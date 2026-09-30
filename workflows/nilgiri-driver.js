export const meta = { name: "nilgiri-driver", description: "Run a Nilgiri MUD driver session from a filled brief file", phases: ["drive"] };

phase("drive");

const inputs = args ?? {};
const briefPath = inputs.brief_path;
const logPath = inputs.log_path;
const inboxPath = inputs.inbox_path;
const sessionSeconds = inputs.session_seconds;
const character = inputs.character || "SinMuseBot";

const report = agent(
  "You are the Nilgiri MUD session driver for " + character + ".\n\n" +
  "Read your full driver brief FIRST: " + briefPath + " — it contains the complete rules (comms protocol, authority order, combat rules, zones, exit procedure). Follow it exactly.\n\n" +
  "Session log: " + logPath + "\n" +
  "Command FIFO: /tmp/mud_cmd\n\n" +
  "Operator inbox: " + inboxPath + " — on EVERY wake, read this file for timestamped operator notes (corrections, live orders). Operator notes override the brief the same way controller speech does. Apply them immediately, then continue.\n\n" +
  "Play the session (" + sessionSeconds + " seconds of game time). The relay announces >>> TIME UP in the log when the budget ends — that is your only normal retirement trigger; the brief states the exact rule.\n\n" +
  "When the session ends, retire cleanly per the brief, verify cleanup (no relay process, no FIFO, no PID files), and return your final report covering: time in/out, XP start/end, confirmed kills with locations, treasure (Dump finds, vault contents, bank balance), lessons learned, and shutdown state.",
  { key: "driver-session", label: "Nilgiri driver session", timeoutMs: (sessionSeconds * 1000) + 1200000 }
);

log("driver session complete");

return { driver_report: report };