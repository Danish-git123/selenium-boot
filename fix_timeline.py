import sys

path = "src/main/java/com/seleniumboot/reporting/HtmlReportGenerator.java"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

old = """     * Gantt-style timeline: one lane per thread, one bar per test positioned by
     * {@code startedAtMs} offset from the earliest start. {@code end = startedAtMs + totalMs}.
<<<<<<< HEAD
     * Tests without {@code startedAtMs} are left out; the card is hidden when none have it (e.g. old history files).
=======
     * Tests without {@code startedAtMs} are skipped (e.g. skipped by dependency); the card is
     * hidden only when no tests remain with usable timing data.
>>>>>>> 025c20a (fix(report): skip tests without startedAtMs in timeline instead of hiding it)
     * Handles single-thread runs and degrades cleanly.
     */
    static String buildTimelineSection(JsonNode tests) {
        if (tests == null || !tests.isArray() || tests.size() == 0) return "";

        java.util.List<TimelineEntry> entries = new java.util.ArrayList<>();
        for (JsonNode test : tests) {
<<<<<<< HEAD
            // Tests that never started (e.g. skipped by dependency) have no start time; leave them out
            long startedAt = test.hasNonNull("startedAtMs") ? test.get("startedAtMs").asLong() : 0L;
=======
            if (!test.has("startedAtMs") || test.get("startedAtMs").isNull()) {
                continue;
            }
            long startedAt = test.get("startedAtMs").asLong();
>>>>>>> 025c20a (fix(report): skip tests without startedAtMs in timeline instead of hiding it)
            if (startedAt <= 0) continue;"""

new = """     * Gantt-style timeline: one lane per thread, one bar per test positioned by
     * {@code startedAtMs} offset from the earliest start. {@code end = startedAtMs + totalMs}.
     * Tests without {@code startedAtMs} are skipped (e.g. skipped by dependency); the card is
     * hidden only when no tests remain with usable timing data.
     * Handles single-thread runs and degrades cleanly.
     */
    static String buildTimelineSection(JsonNode tests) {
        if (tests == null || !tests.isArray() || tests.size() == 0) return "";

        java.util.List<TimelineEntry> entries = new java.util.ArrayList<>();
        for (JsonNode test : tests) {
            if (!test.has("startedAtMs") || test.get("startedAtMs").isNull()) {
                continue;
            }
            long startedAt = test.get("startedAtMs").asLong();
            if (startedAt <= 0) continue;"""

if old in content:
    content = content.replace(old, new)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("fixed")
else:
    print("not found")
