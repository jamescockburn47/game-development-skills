/* The readable game description, research and development record. */
function renderGamePlan(data) {
  const byId = id => document.getElementById(id);
  const make = (tag, text, className) => {
    const node = document.createElement(tag);
    if (text !== undefined) node.textContent = text;
    if (className) node.className = className;
    return node;
  };
  byId('plan-version').textContent = `Version ${data.revision}${data.development ? ` · Updated ${data.development.updated}` : ''}`;
  if (data.archived_view) {
    const notice = make('p', 'You are reading an earlier saved copy. ', 'archive-notice');
    const current = make('a', 'Open the current plan');
    current.href = data.current_url;
    notice.append(current);
    document.querySelector('.header-copy').append(notice);
    document.querySelector('.action-panel').hidden = true;
  }
  if (!data.game) {
    document.querySelectorAll('.review-nav a[href="#game-section"], .review-nav a[href="#progress-section"]').forEach(link => { link.hidden = true; });
    document.querySelector('.skip-link').href = '#decisions-title';
    return;
  }
  byId('game-section').hidden = false;
  byId('user-description').hidden = data.schema_version !== 3;
  byId('legacy-game').hidden = data.schema_version === 3;
  if (data.schema_version === 3) {
    byId('game-premise').hidden = true;
  } else {
    byId('game-title').textContent = 'Earlier game description';
    for (const field of ['premise', 'role', 'goal', 'arc', 'style']) byId(`game-${field}`).textContent = data.game[field];
    for (const beat of data.game.session) {
      const li = make('li');
      li.append(make('strong', beat.title), make('p', beat.detail));
      byId('game-session').append(li);
    }
    byId('game-section').append(make('p', 'This older format does not record a user-written description. Supply your own description before approving any new build.'));
  }
  byId('inspiration-section').hidden = false;
  for (const example of data.inspirations) {
    const card = make('article', undefined, 'inspiration-card');
    card.append(make('h3', example.title), make('p', example.observation));
    for (const [heading, text] of [['What we could learn', example.lesson], ['Our own direction', example.difference]]) {
      const para = make('p');
      para.append(make('strong', `${heading}: `), document.createTextNode(text));
      card.append(para);
    }
    const link = make('a', `Explore ${example.title} ↗`);
    link.href = example.url;
    link.target = '_blank';
    link.rel = 'noopener noreferrer';
    card.append(link, make('p', `Source checked ${example.checked} · Opens online`, 'meta'));
    byId('inspirations').append(card);
  }
  if (!data.inspirations.length) byId('inspirations').append(make('p', 'No reference examples have been researched yet. You can suggest one in your reply.'));
  const dev = data.development;
  const stages = { idea: 'Planning the game', building: 'Making the game', testing: 'Trying it with players', released: 'Available to players' };
  const states = { planned: 'Still to do', in_progress: 'Under way', done: 'Done', revisit: 'Needs another look' };
  byId('progress-section').hidden = false;
  byId('progress-summary').textContent = dev.summary;
  byId('progress-stage').textContent = stages[dev.stage];
  byId('progress-next').textContent = dev.purpose !== 'update' ? dev.next :
    dev.next === 'none' ? 'No further work is planned.' : data.next_steps[Number(dev.next.split(':')[1]) - 1].title;
  for (const entry of dev.milestones) {
    const li = make('li');
    li.append(make('strong', `${entry.title} — ${states[entry.status]}`), make('p', entry.detail));
    if (entry.evidence) li.append(make('p', `What supports this: ${entry.evidence}`));
    byId('progress-items').append(li);
  }
  if (!dev.milestones.length) byId('progress-items').append(make('li', 'We will add progress here as work begins.'));
  byId('progress-history').append(make('li', `This version: ${dev.change_note || data.summary}`));
  for (const entry of data.history_links || []) {
    const li = make('li');
    const link = make('a', `Version ${entry.revision}`);
    link.href = entry.url;
    li.append(link, make('p', `${entry.date ? `${entry.date} · ` : ''}${entry.summary}`));
    byId('progress-history').append(li);
  }
  if (!data.history_links?.length) byId('progress-history').append(make('li', 'This is the first saved plan in this folder.'));
  const agreed = dev.approved_plan;
  byId('progress-approval').textContent = dev.purpose === 'update' ?
    `Progress report on the work agreed in version ${agreed.revision}. You can give feedback here; this page does not ask you to approve that work again.` :
    `This is a proposed plan. ${agreed ? `Version ${agreed.revision} records the earlier agreement. ` : ''}The work described here waits for your agreement.`;
  if (data.example) byId('progress-approval').prepend(document.createTextNode('Example only. '));
  if (dev.purpose === 'update') {
    byId('approve-review').hidden = true;
    byId('request-revision').textContent = 'Give feedback';
    document.querySelector('.scope-banner').hidden = true;
  }
}
