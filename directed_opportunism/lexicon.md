# Lexicon — the book's terms as the book means them

Why this exists (the CEO, 2026-10-20, directed_opportunism `state/ceo_words_2026-10-20.md`): "we cannot just use plain intent we need to define exactly what words mean in context of the book … intent in general is not exactly what the book means … it can create far different outcome considering if its looked through the llm defaults specially when we wont pass whole book to the projects that use the tool".
Each entry: **Book**: the book's own defining words, quoted, with the book's page · **Not**: the everyday or AI-world meaning an agent will reach for by default [interp].
The CEO, same day: "all the terms we had to use so far need to be defined clearly for example high level intent is not same as intent". So the lexicon covers the terms in use: the book's terms (parts 1–5), the book's near-terms that must not be merged (part 6), and words to avoid (part 7). A 'Here' line says how a folder that uses the method applies the term; where a file's path differs between folders, AGENTS.md names it. The lexicon's history: directed_opportunism `evidence/lexicon_history.md`. Read part 7 first: those are the everyday words an agent reaches for, in a reply as much as in a file.

## 1. The problem
**Friction**
- Book: "Friction is a function of the finitude of the human condition – the fact that our knowledge is limited and the fact that we are independent agents" (p.40).
- Not: annoyance, UX friction, "frictionless".

**The three gaps**
- Book: "We could name the gap between outcomes and plans the knowledge gap, the gap between plans and actions the alignment gap, and the gap between actions and outcomes the effects gap … All three are the result of friction" (p.45).
- Not: skills gap, knowledge base, alignment in the AI-safety sense.

## 2. The answer
**Directed opportunism**
- Book: "The name I have chosen for mission command in business is 'directed opportunism.'" The result is "an organization whose actions cohere because it is following a clear direction, and seizes unexpected opportunities because individuals and groups adapt as they go" (p.85). "So the 'plan-and-implement model' of strategy becomes a 'do-and-adapt' model" (p.86).
- Not: opportunism (taking any chance), "agile", improvising without direction.

**Directive (not order)**
- Book: "the senior commander was not to tell his subordinate how he was to accomplish his task, as he would if were to issue an order … The intention was binding; the task was not" (p.71).
- Not: an instruction to be executed as written.

**Independent thinking obedience**
- Book: "General von Schlichting, coined the phrase selbstständig denkender Gehorsam – 'independent thinking obedience.'" (p.70). "A German officer's prime duty was to reason why" (p.71).
- Not: obedience (do as told), nor independence (do as you like); not "agreeing with the user".

**Information-processing capacity; the available level of information**
- Book: van Creveld: "Confronted with a task, and having less information available than is needed to perform that task, an organisation may react in either of two ways. One is to increase its information-processing capacity, the other to design the organisation, and indeed the task itself, in such a way as to enable it to operate on the basis of less information" (p.144). Structure the tasks "in such a way that the units can perform the tasks with the available level of information" (p.146).
- Here: an LLM agent's information-processing capacity is its context window and the attention its model gives within it; as a task fills it, each part may get less [hyp: trial 11 did not show lost depth]. Judge it by the parts that each need their own reading and judgment, not by whether the whole fits the context. Dividing the task among subordinates, each with a brief, is van Creveld's second way [interp; the CEO: "division of attention to many steps dilutes the attention quality instead of focusing attention on one task only doing it well and passing result up", directed_opportunism `state/ceo_words_session_63dfc8e4.md`].
- Not: a larger context window or a stronger model as the answer (the first way); "it fits in my context, so it is one task".

## 3. Direction
**Intent**
- Book: "An intent is the decision to do something now (a task) in order to achieve an outcome (a purpose). The decision will be a function of the situation and the aim" (p.110). "Intent is expressed in terms of what to achieve and why" (p.65). "Alignment needs to be achieved around intent, and autonomy should be granted around actions" (p.65).
- Not: a wish, a goal statement, a vision, a mission statement; and in the AI world, **"user intent"** (classifying what a user wants from a message). The book's intent is a **decision**, about **now**, that links a **task** to a **purpose**, made from the **situation** and the **aim**.

**Task** and **purpose**
- Book: task = "to do something now"; purpose = "an outcome" (p.110). "Commanders do this by issuing missions rather than tasks (a mission is a task + a purpose)" (p.257, quoting British military doctrine).
- Not: task = a ticket or to-do item; purpose = a value or "higher purpose".

**Aim**
- Book: "Let us call this element the aim. An aim can be an end-point or destination, and aiming means pointing in that direction, so it encompasses both 'going west' and 'getting to San Francisco.' The aim defines what the organization is trying to achieve" (p.101).
- Not: a target number or a KPI.

**End-state**
- Book: "the end-state is not arbitrary … The end-state is determined by insights gained from an analysis of the existing situation" (p.119).
- Not: a dream, "far blue yonder" (p.119), a vision board.

**Situation (Context)**
- Book: "An account of the situation, bringing out the essential features which bear on the course of action to be taken. It is useful to cover the state of knowledge, distinguishing what is known, what is probable but uncertain, and what is not known" (p.137, continuing "but could be relevant").
- Not: background, everything known, a project summary.

**Higher intent** (one and two levels up)
- Book: "the explicit articulation of the intention both one and two levels above. In other words, I have to understand both what my boss and their boss in turn are trying to achieve" (p.172).
- Not: a higher purpose, values, mission statement.

**Main effort**
- Book: "The main effort is that single thing which will either in itself have the greatest impact or on which all other things depend. It has resourcing priority" (p.122). "If our intent is to gain market share in order to strengthen our long-term position, the main effort is revenue and holding margin at 15 percent is a constraint" (p.166).
- Not: the top of a priority list, where most work goes, "focus areas" (plural).

**Implied tasks**
- Book: "The acid test of understanding is being able to say what the message implies about what an individual should do" (p.171). Joe's "four implied tasks laid out how they were going to achieve their overall task, and each was made the responsibility of one member of the team" (p.169).
- Not: implicit requirements guessed from vague input; sub-steps of a to-do list.

**Boundaries: freedoms and constraints**
- Book: "Constraints do not only define boundaries, but help to clarify what is wanted by making explicit what is not wanted. They may take the form of what have been called 'anti-goals'" (p.138). "I can determine how much space to give you by setting the boundaries and the control loop. The default is to give you as much as possible" (p.191). "The boundaries should be set so that failure is not catastrophic" (p.191).
- Not: guardrails, policies, rules, safety filters.

## 4. Linking levels
**Strategy briefing** (military: mission analysis)
- Book: "In a military organization using mission command, this discipline is called 'mission analysis.' In the language I have developed for business, I call it 'strategy briefing.'" (p.148). "The purpose of briefing is to enable people to act independently" (p.164). The template "looks like a form, it is really a set of concepts to help to structure thinking" (p.170).
- Here: written down ("First, a briefing is written down. This ensures that it has been heard", p.171) in the template's six parts (pp.249–250); the CEO's direct subordinate's is `BRIEF.md`, a subordinate's is its brief for one task.
- Not: a briefing as a presentation, a status update, a handover summary.

**Backbrief**
- Book: "In the backbrief three things happen": the unit "checks its understanding of the direction it has received or worked out"; "the superior gains clarity for the first time about what the implications of their own directions actually are, and may revise them"; and "it provides an opportunity to ensure alignment across the organization as well as up and down it" (p.168).
- Not: a status report, a summary of work done, a read-back for approval.

**Has the situation changed?**
- Book: "No – our brief is valid • Yes – we have to change some tasks, but what we are trying to achieve is still valid • Yes – and we have to change what we are trying to achieve" (p.250).
- Not: "any updates?"

## 5. Control
**Command and control**
- Book: "Control is the ability to adjust, which means knowing what is actually happening and having some means of affecting it … no act of command can be derived from any act of control" (p.210).
- Not: command-and-control management (top-down micromanagement).

**Control loop**
- Book: "I can make the boundaries narrower, and I can make the control loop tight or loose" (p.191).
- Not: a feedback loop in control engineering; **an agent loop** (the AI-world default: an agent repeatedly calling tools).

**Measures**, **the dashboard**, **readings**
- Book: "the measures are just there to tell us whether we are successful or not. What we are trying to optimize is the outcome. The measures are the dashboard. We’ve got a speedometer, a milometer, and a fuel gauge. We need to watch them, but we should not confuse the readings on them with what we really want to do, which is to arrive on time at our destination" (p.158). So: a measure is a gauge; a reading is what it shows now; the dashboard is the measures together.
- The book's negative example, same page: Joe's bonus was tied to the number of new products; "Optimizing that was not difficult – he could merely go for the easy ones nearest completion. Whether they had any impact or not was somebody else’s problem" (p.158). A reading optimized in place of the outcome.
- Not: KPIs as goals, acceptance criteria as the purpose; "readings" as interpretations (for those we say interpretation, the book's word: "open to different interpretations", p.35); a dashboard as a UI screen.

**Manager's letter**
- Book: as management by objectives became a process, "The 'manager's letter' became an approval process rather than a backbrief" (p.239).
- Not: a cover letter, a report for approval.

**Strategy, operations, tactics**
- Book: "Strategy is about winning wars and involves armies; operations is about winning campaigns …; tactics is about winning battles" (p.219). "Tactics specify how to do things and are binding on everyone" (p.220).
- Not: strategy = a plan; tactics = tricks.

**Reviews** (the book's)
- Book: "The main theme of the reviews is the question: 'Has the situation changed?'" (p.202).
- Not: a code review, an audit, an approval.

**Upward delegation**
- Book: "their default behavior pattern is to delegate upward by continually asking for direction" (p.183).
- Not: escalation of a real blocker (that is "refer back", p.174).

**Plan**
- Book: "Strategy is essentially an intent rather than a plan, because the knowledge gap means that we cannot plan an outcome but only express the will to achieve it" (p.110).
- Not: interchangeable with intent; a plan is one way to carry an intent out.

**Targets**
- Book: "If we hit our targets and don't fulfill the purpose, we should not congratulate ourselves" (p.208).

**Levels and the cascade**
- Book: "The overall direction should be communicated in a cascade. Direction from the highest level should be kept high level. The levels below add appropriate detail. Each level is guided by the intention of the one above" (p.62). "Briefing and backbriefing are repeated at each level" (p.148).
- Not: management layers as reporting lines; "layer" in software.

**Superior, boss, subordinate**
- Book: the template's "One level up (my boss) Two levels up (my boss's boss)" (p.249); "subordinates" (p.62).

**Assign, brief**
- Book: "they need to break down their task into further tasks implied by their main one, assign them, and pass the message on" (p.148); "A briefing should cover the higher intent, up to two levels up, the tasks that this implies for the unit concerned, where their main effort should lie, and their freedoms and constraints" (p.175).
- Not: spawn, launch, fork, delegate a job.

**Operating principle**
- Book: Napoleon's marshals "shared a few operating principles (such as “always march toward the sound of the guns”)" (p.55); that rule puts into practice "the behavioral principle of mutual support" (p.242).
- Here: START_TEXT's three; each carries the book's principle it applies, since a principle in a section above them changed no action [evidence, directed_opportunism `evidence/trials/trial_5.md` to `trial_7.md`].
- Not: a rule, a guideline, a best practice.

**The CEO** (the CEO, 2026-10-23: "directed opportunism so if commander is highest authority then use CEO")
- Book: "the man at the top" (p.186); "if the CEO were to change his intentions mid-year" (p.202). And what a CEO must do beyond having direction: of one who "has the focus and direction of a good CEO" but "doesn't give clear, direct orders", the book says "Knowing what you want is not enough. You also have to be able to actually set direction" (p.131). [interp: one person at the top of the business, whose intentions the rest follow.]
- Here: the person at the top of directed_opportunism and every project, who sets each one's direction as intent (the CEO's intent for a folder; AGENTS.md names its file). The name says whose intent and words are the source (quoted with their file) and whom an agent asks when a project's intent is unclear ("its agent asks me").
- The book's "commander" is another word: it has a commander at every level ("the senior commander", p.71; "The commander of 26th Infantry Brigade", p.68). In a quote ("the higher commander", p.71; "a commander's intent", p.179) it means the superior at that level, not the CEO.
- Not: the "CEO-heroes" the book warns of, with "the delusion that one can control external events (i.e., a denial of friction)" and "a concomitant tendency to command a great deal more than is necessary" (p.100); "the owner of each task" (p.173), which here is the subordinate the task is assigned to; a user giving orders (see **Directive (not order)**).

**The CEO's direct subordinate** (the CEO: "too generic" for the name it replaced; its relation to the intent must show)
- Book: a briefing covers "the higher intent, up to two levels up" (p.175); the template's "Higher intent: One level up (my boss) / Two levels up (my boss’s boss)" (p.249). A senior commander should retain "a clear picture of the overall situation" (p.61) [interp: here that is the CEO's direct subordinate, who holds the common map; "the man at the top" is the CEO].
- Here: the agent directly under the CEO, one level below the CEO. The CEO's intent for its folder (AGENTS.md names the file) is its higher intent one level up, and two levels up for each subordinate it briefs. It holds the common map, not the tasks (pp.61, 238). Not "line", which in the book means commanders as against staff (pp.27, 67).
- Not: the orchestrator, the manager, the main agent; "the top" with no relation to the intent.

**Staff officer** (the CEO: "if book has better defined and more clear words then use them")
- Book: von Moltke "had his own staff officers visit units and report back to him what they saw" (p.212). At the front, "One of von Moltke’s staff officers was with him and confirmed that the intention was to hold the French in position" (p.68); the next day "one of von Moltke’s staff officers assured von der Goltz that “his course of action had eminently furthered the objects aimed at" (p.69): an action judged against the intent. The book's umpire is another thing: in wargames "He replaced the original dice with an umpire to increase realism and add to the level of friction" (p.179).
- Here: a subordinate given the staff officer brief whole (AGENTS.md names its file) and holding that task alone. It judges the work (files, trials) against the CEO's intent, the CEO's words, and the book where the folder holds it, and reports what it saw to the one who briefed it [interp: in the book they report to von Moltke (p.212) or give their verdict to the one who acted (p.69); here they report to whoever briefed them, usually the CEO's direct subordinate]. It holds no command: it decides nothing and changes nothing; the one who briefed it decides. Why agents need it [interp]: the agent that makes an adjustment does not see the gaps that adjustment opens; staff officer runs caught points the adjusting agent had passed [evidence, directed_opportunism `evidence/session_63dfc8e4.md`]. How it works in agents is directed_opportunism's to decide, as the CEO's boundary says ("questions about applying the method are answered by this project"; "this project" there is directed_opportunism).
- Not: a reviewer who fixes what it finds; an approver; a test suite; an umpire in the book's sense (p.179).

**Battle group**
- Book: the German Army retained the ability "to change structure rapidly at all levels, forming “battle groups,” often named after their commander, to carry out specific tasks" (p.144).
- Not: a team, a squad of workers.

**Adjust**
- Book: "Adjustment follows" (p.168); "It is through measures that we know how to adjust and when a task is completed" (p.174); "So the 'plan-and-implement model' of strategy becomes a 'do-and-adapt' model" (p.86).
- Not: fixing a bug, patching, a one-off repair.

**Adopt**
- Book: "Adopting mission command as an operating model is not a matter of setting up some processes, but of mastering some skills, perhaps more precisely called 'disciplines.' Only when those skills have been mastered can the process be adopted" (p.81); mission command "could take root quite quickly" (p.83).
- Not: install, deploy, set up, copy files in.

**Common map** (the CEO, 2026-10-21: "my map is aimed to be easy to visualize mentally a story that allows easily to grasp how something contributes to the intent")
- Book: Reports ("Field Memoranda") "create a common map of the situation, collective progress to date, current priorities and everybody's part in the plan" (p.238).
- Here: the CEO's direct subordinate's `MAP.md`: the situation, progress and where we stand; that level's tasks are in its strategy brief, `BRIEF.md`. The two together are what the CEO calls the handoff ("read handoff", "update handoff").
- Not: a diagram, a dashboard, a status log.

**The map's story words** (the CEO, 2026-10-20: "it needs to be like explaining situation as an story in the map"; the book has no terms for these, so they are defined here)
- Campaign: the book's word ("operations is about winning campaigns", p.219); here, all the work toward the CEO's intent.
- Story: the map's account of the campaign as the CEO's direct subordinate understands it; numbered, and retold under a new number when a new brief comes.
- Point 0: where the campaign started.
- Leg: a stretch of the campaign between two changes of direction or structure; each ends with how it bears on the CEO's intent ("For the intent:").
- The ground: what the work meets in this field (agents with no memory, files, words), known only where walked.
- Roads opened, roads closed: courses of action found to lead toward the intent, or found not to (the book's "the course of action to be taken", p.137).
- Not: a user story, a sprint, a milestone, a roadmap.

**Our own working words** (the book has no terms for these; defined here, as the CEO asks: "if need to invent words they need to be clearly defined")
- Entry: the file an agent reads first: `AGENTS.md`, for any agent; Claude Code reaches it through `CLAUDE.md`.
- Trial: a test of the files on fresh agents, what was expected written down before it runs, judged by a staff officer [directed_opportunism `evidence/trials/`]. Nearest in the book: the staff ride, where candidates were asked "to assess the ground, the situation, and the options" (p.178) [interp].
- Round: one staff officer's check and the adjustment of what it found.
- Not: a clinical trial; a tournament round.

**Staff and doctrine**
- Book: "They needed a common operational doctrine and shared values" (p.71); "a common doctrine based on principles rather than rules" (p.180).
- Not: staff = employees; doctrine = dogma.

## 6. Near-terms the book keeps apart (never merge them)
| Term | The book's meaning | Page |
|---|---|---|
| **intent** | "the decision to do something now (a task) in order to achieve an outcome (a purpose)" | p.110 |
| **higher intent** | the intent of the level above (my boss) and two levels above (my boss's boss) | pp.172, 249 |
| **overall intention** | the intention of whoever issues the directive, binding all below it (at the highest level, the CEO's): "freedom to act within the boundaries set by the overall intention. The intention was binding; the task was not" | pp.62, 71 |
| **aim** | "what the organization is trying to achieve"; a direction or a destination | p.101 |
| **end-state** | where the aim leads, "determined by insights gained from an analysis of the existing situation" | p.119 |
| **"strategic intent"** | Hamel and Prahalad's term; the book: "It is what we have called an endstate" | pp.115–116 |
| **"high level"** | not a kind of intent: how much detail direction carries. "Direction from the highest level should be kept high level. The levels below add appropriate detail" | p.62 |
| **mission** | "a task + a purpose" (doctrine quoted) | p.257 |
| **purpose** | the outcome a task serves | p.110 |
| **outcome** | what is achieved in the world; measures only indicate it | pp.110, 158 |
| **goal, objective** | the book's synonyms for its "what" and "why" in other companies' usage; the book's own word is intent | p.164 |
So "the top-level intent" in our talk means the **overall intention** at the highest level (the CEO's), not an intent of a special kind; for a project it is the project's **higher intent**.


## 7. Words to avoid (they pull to the defaults)
| Avoid | Use instead | Why |
|---|---|---|
| goal, objective, vision, mission statement | intent / aim / end-state as defined above | everyday management words; the book's distinctions disappear |
| high-level intent, top-level intent | the overall intention (at the highest level, the CEO's) / higher intent (for the level below) | not book terms; "high level" is about detail (p.62) |
| priority, top priorities | main effort (one) | a priority list has many; main effort has one (p.122) |
| requirements, specs (for direction) | intent + boundaries | requirements describe hows |
| rules, guardrails, policies (for boundaries) | constraints, freedoms | boundaries define space, not procedure (p.191) |
| instructions, orders (for direction to a project) | directive / brief | an order specifies the how (p.71) |
| "what and why" as a name or definition for intent | intent (defined above) | the book defines intent itself (p.110); its own "what" and "why" stay where it uses them (p.65; the template, p.249) |
| agent loop (for the control loop) | control loop: how often to report | AI-world default |
| user intent | the CEO's intent | AI-world default |
| drift | the knowledge gap, the alignment gap or the effects gap (p.45), whichever it is; all three when it is not one ("we must address all three", p.53) | the CEO, 2026-10-21: "from now on we will use gaps instead of drift"; the book uses "drifted" only inside the trade-off view it rejects (p.64) and for organizations sliding away from mission command (p.83) |
| fix, fixing | adjust, adjustment | the book's word (pp.86, 168, 174) |
| install | adopt | p.81: adopting is "mastering some skills", not "setting up some processes" |
| spawn, launch (a subagent) | assign a task and brief a subordinate | p.148; the CEO, 2026-10-21: "spawn which is wrong word" |
| worker | subordinate | p.62 |

## Not yet covered (add only when a review shows it is misread)
center of gravity (p.103), Auftragstaktik (pp.70–77), trust (pp.189–191).
