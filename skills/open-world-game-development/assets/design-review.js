(() => {
  'use strict';
  const data = JSON.parse(document.getElementById('review-data').textContent);
  const byId = id => document.getElementById(id);
  const make = (tag, text, className) => {
    const node = document.createElement(tag);
    if (text !== undefined) node.textContent = text;
    if (className) node.className = className;
    return node;
  };
  const labels = { user: 'You asked for this', agent: 'Our suggestion', assumption: 'Our best guess' };
  const progressOnly = data.development?.purpose === 'update';
  const readOnly = data.archived_view === true;
  const ownsDescription = data.schema_version === 3;
  const originalDescription = ownsDescription ? data.game.description : '';
  let description = originalDescription;
  renderGamePlan(data);
  const references = new Map([
    ...data.next_steps.map((step, index) => [`step:${index + 1}`, { label: `Step ${index + 1}`, text: step.title }]),
    ...data.acceptance.map((check, index) => [`check:${index + 1}`, { label: `Check ${index + 1}`, text: check }])
  ]);
  const referenceLink = (ref, detailed = false) => {
    const target = references.get(ref);
    const link = make('a', detailed ? `${target.label}: ${target.text}` : target.label);
    link.href = `#${ref.replace(':', '-')}`;
    return link;
  };
  const baseline = Object.fromEntries(data.decisions.map(item => [item.id, item.value]));
  let values = { ...baseline };
  let notes = '';
  let storageWarning = '';
  let response = null;
  const storageKey = `game-design-review:${data.review_id}:${data.fingerprint}`;
  const allowed = (item, value) => typeof value === 'string' && value.trim() && value.length <= 2000 &&
    (item.editable !== false || value === item.value) &&
    (!item.options?.length || item.options.some(option => option.value === value));
  try {
    const stored = JSON.parse(localStorage.getItem(storageKey) || 'null');
    if (stored && !readOnly) {
      if (!stored.values || Object.keys(stored.values).length !== data.decisions.length ||
          typeof stored.notes !== 'string' || stored.notes.length > 3000 ||
          !data.decisions.every(item => allowed(item, stored.values[item.id]))) throw new Error('Invalid stored draft');
      values = { ...stored.values };
      notes = stored.notes;
      if (ownsDescription) {
        if (typeof stored.game_description !== 'string' || stored.game_description.length > 12000) throw new Error('Invalid stored description');
        description = stored.game_description;
      }
    }
  } catch (error) {
    storageWarning = 'Local draft storage is unavailable or invalid. Copy your response before closing.';
  }
  const changed = () => data.decisions.filter(item => values[item.id] !== item.value);
  const descriptionChanged = () => description !== originalDescription;
  const hasDescription = () => ownsDescription && !!originalDescription.trim() && !!data.game.recorded_from;
  const dirty = () => changed().length > 0 || notes.trim().length > 0 || descriptionChanged();
  const valid = () => data.decisions.every(item => allowed(item, values[item.id])) && description.length <= 12000;
  const save = () => {
    try { localStorage.setItem(storageKey, JSON.stringify({ values, notes, game_description: description })); }
    catch (error) { storageWarning = 'Local saving is unavailable. Copy your response before closing.'; }
  };
  const fillList = (id, items, emptyText) => {
    const list = byId(id);
    list.replaceChildren(...(items.length ? items : [emptyText]).map(item => make('li', item)));
  };
  byId('review-title').textContent = data.title;
  document.title = `${data.title} — game plan`;
  byId('review-summary').textContent = data.summary;
  byId('build-scope').textContent = data.scope;
  byId('review-meta').textContent = `Revision ${data.revision} · ${data.review_id} · ${data.fingerprint.slice(0, 10)}`;
  byId('decision-count').textContent = String(data.decisions.length);
  byId('demo-notice').hidden = !data.example;
  byId('review-notes').value = notes;
  if (ownsDescription) {
    byId('game-description').value = description;
    byId('game-description').readOnly = readOnly;
    byId('game-description').addEventListener('input', event => { description = event.target.value; invalidate(); });
  }
  for (const [index, check] of data.acceptance.entries()) {
    const li = make('li', `Check ${index + 1}: ${check}`);
    li.id = `check-${index + 1}`;
    byId('acceptance').append(li);
  }
  fillList('boundaries', data.boundaries, 'Nothing else has been set aside.');
  fillList('risks', data.risks, 'Nothing else to flag at this stage.');
  fillList('questions', data.open_questions, 'No unanswered questions are holding up the next step.');
  for (const [index, step] of data.next_steps.entries()) {
    const li = make('li');
    li.id = `step-${index + 1}`;
    li.append(make('h3', step.title), make('p', step.detail));
    byId('next-steps').append(li);
  }
  const cards = new Map();
  for (const item of data.decisions) {
    const card = make('article', undefined, 'decision-card');
    card.dataset.decisionId = item.id;
    const heading = make('div', undefined, 'decision-heading');
    const label = make('label', item.label);
    label.htmlFor = `choice-${item.id}`;
    heading.append(label, make('span', labels[item.source], `badge source-${item.source}`));
    let input;
    if (item.options?.length) {
      input = make('select', undefined, 'decision-input');
      for (const option of item.options) {
        const node = make('option', option.label);
        node.value = option.value;
        input.append(node);
      }
    } else {
      input = make('textarea', undefined, 'decision-input');
      input.rows = 2;
      input.maxLength = 2000;
    }
    input.id = `choice-${item.id}`;
    input.value = values[item.id];
    input.disabled = readOnly || item.editable === false;
    input.required = true;
    const rationale = make('p', item.rationale, 'rationale');
    rationale.id = `reason-${item.id}`;
    input.setAttribute('aria-describedby', rationale.id);
    const impact = make('p', undefined, 'impact');
    const affected = make('p', 'Affects: ', 'rationale');
    item.affects.forEach((ref, index) => {
      if (index) affected.append(document.createTextNode(' · '));
      affected.append(referenceLink(ref));
    });
    const marker = make('span', 'Changed — we’ll update the plan', 'change-label');
    marker.hidden = true;
    card.append(heading, input, rationale, impact, affected, marker);
    if (item.editable === false) card.append(make('p', 'You asked us to keep this. To change it, leave a note below.', 'locked-note'));
    input.addEventListener('input', () => { values[item.id] = input.value; invalidate(); });
    byId('decisions').append(card);
    cards.set(item.id, { card, input, impact, marker });
  }
  byId('decisions').setAttribute('aria-busy', 'false');
  function render() {
    const edits = changed();
    const isDirty = dirty();
    const isValid = valid();
    const filter = byId('filter-select').value;
    for (const item of data.decisions) {
      const nodes = cards.get(item.id);
      const hasChanged = values[item.id] !== item.value;
      nodes.card.classList.toggle('changed', hasChanged);
      nodes.marker.hidden = !hasChanged;
      nodes.card.hidden = (filter === 'changed' && !hasChanged) || (filter === 'recommended' && item.source === 'user');
      nodes.input.setAttribute('aria-invalid', String(!allowed(item, values[item.id])));
      const option = item.options?.find(choice => choice.value === values[item.id]);
      nodes.impact.textContent = option?.impact || 'If you change this, we’ll update the parts linked below.';
    }
    byId('changes-count').textContent = String(edits.length + Number(descriptionChanged()));
    if (ownsDescription) byId('description-status').textContent = descriptionChanged() ?
      'Your draft is saved locally. Return it in chat so we can update the plan around your words.' :
      hasDescription() ? 'Your wording is kept as supplied. You can edit it here when your idea changes.' :
      'Waiting for your description. The AI will not write this for you; planning follows your reply.';
    byId('change-notice').hidden = !isDirty;
    const areas = [...new Set(edits.flatMap(item => item.affects))];
    const detail = byId('change-impact');
    detail.replaceChildren(make('p', 'Your edits have not been sent. Your words remain yours; we’ll review the affected choices and next steps when you return your reply.'));
    if (descriptionChanged()) detail.append(make('p', 'Your game description changed. We’ll check the whole plan against it and show you any revised recommendations before building.'));
    if (areas.length) {
      const list = make('ul');
      for (const ref of areas) {
        const li = make('li');
        li.append(referenceLink(ref, true));
        list.append(li);
      }
      detail.append(list);
    }
    if (notes.trim()) detail.append(make('p', 'We’ll include your notes when we update the plan.'));
    byId('approve-review').disabled = readOnly || progressOnly || !hasDescription() || isDirty || !isValid || data.open_questions.length > 0 || data.example === true;
    byId('request-revision').disabled = readOnly || !isValid;
    let status = !hasDescription() ? (ownsDescription ? 'Write your description and return it in chat. We need your words before planning or building.' :
      'This is an older plan. Supply your own game description before approving a new build.') :
      data.example ? 'This is a sample. Try changing a choice and selecting Suggest changes. Agreement is turned off.' :
      !isValid ? 'Fill in the empty choices before preparing your reply.' :
      isDirty ? 'Return your changes in chat. We’ll show you an updated plan before acting on them.' :
      data.open_questions.length ? 'We need to settle the questions before you agree to the plan.' :
      progressOnly ? 'This is a progress update. You can leave feedback; the agreed work can continue.' :
      'Read the plan and tell us what you think. Nothing has been agreed or sent yet.';
    if (response) status = 'Your reply is ready. Copy or download it and return it in chat. It has not been sent yet.';
    byId('review-status').textContent = [status, storageWarning].filter(Boolean).join(' ');
    byId('response-panel').hidden = !response;
  }
  function invalidate() {
    response = null;
    byId('response-output').value = '';
    save();
    render();
  }
  function prepare(decision) {
    if (readOnly || !valid()) return;
    if (decision === 'approve' && (progressOnly || !hasDescription() || dirty() || data.open_questions.length || data.example)) return;
    response = { schema_version: ownsDescription ? 2 : 1, review_id: data.review_id, revision: data.revision,
      fingerprint: data.fingerprint, decision, values: { ...values }, notes, example: data.example || false };
    if (ownsDescription) response.game_description = description;
    byId('response-output').value = JSON.stringify(response, null, 2);
    const displayValue = (item, value) => item.options?.find(option => option.value === value)?.label || value;
    const edits = changed().map(item => `${item.label}: ${displayValue(item, item.value)} → ${displayValue(item, values[item.id])}.`);
    if (descriptionChanged()) edits.unshift(`Your game description:\n${description}`);
    byId('response-summary').textContent = decision === 'approve' ?
      `You agree with ${data.title}, version ${data.revision}, and the work described in it. Copy or download your reply and send it in chat to confirm.` :
      [`Your feedback on ${data.title}, version ${data.revision}.`, ...edits, notes.trim() ? `Your note: ${notes}` : '',
        'Copy or download your reply and return it in chat.'].filter(Boolean).join('\n\n');
    byId('response-details').open = false;
    render();
    byId('copy-response').focus();
  }
  byId('review-notes').addEventListener('input', event => { notes = event.target.value; invalidate(); });
  byId('filter-select').addEventListener('change', render);
  byId('approve-review').addEventListener('click', () => prepare('approve'));
  byId('request-revision').addEventListener('click', () => prepare('request_changes'));
  byId('reset-review').addEventListener('click', () => {
    values = { ...baseline };
    notes = '';
    description = originalDescription;
    if (ownsDescription) byId('game-description').value = description;
    byId('review-notes').value = '';
    for (const item of data.decisions) cards.get(item.id).input.value = item.value;
    invalidate();
  });
  byId('copy-response').addEventListener('click', async () => {
    if (!response) return;
    const text = byId('response-output').value;
    try {
      await navigator.clipboard.writeText(text);
      byId('review-status').textContent = 'Copied. Paste your reply into chat. Nothing was sent automatically.';
    } catch (error) {
      byId('response-details').open = true;
      byId('response-output').focus();
      byId('response-output').select();
      byId('review-status').textContent = 'Copying was blocked by the browser. Copy the selected response manually, then paste it in chat.';
    }
  });
  byId('download-response').addEventListener('click', () => {
    if (!response) return;
    const blob = new Blob([byId('response-output').value], { type: 'application/json' });
    const url = URL.createObjectURL(blob);
    const link = make('a');
    link.href = url;
    link.download = `${data.review_id}-r${data.revision}-${response.decision}.json`;
    link.click();
    setTimeout(() => URL.revokeObjectURL(url), 1000);
    byId('review-status').textContent = 'Your reply is ready to download. Attach the file in chat; it has not been sent yet.';
  });
  render();
})();
