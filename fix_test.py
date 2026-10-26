import sys
path="src/test/java/com/seleniumboot/unit/TimelineReportTest.java"
c=open(path).read()
old="""    @Test
<<<<<<< HEAD
    public void testWithoutStartedAtMs_isSkippedButOthersStillRender() throws Exception {
        String html = timeline(\"\"\"
                [
                  {"testId":"a","thread":"main","status":"PASSED","totalMs":100,"startedAtMs":1000},
                  {"testId":"b","thread":"main","status":"SKIPPED"}
                ]
                \"\"\");
        Assert.assertTrue(html.contains("timeline-card"), html);
        Assert.assertEquals(count(html, "gantt-bar "), 1, html);
=======
    public void skippedTestWithoutStartedAtMs_doesNotHideTimeline() throws Exception {
        String html = timeline(\"\"\"
                [
                  {"testId":"com.x.A.ran","thread":"pool-1-thread-1","status":"PASSED","totalMs":100,"startedAtMs":1000},
                  {"testId":"com.x.B.skipped","thread":"pool-1-thread-1","status":"SKIPPED","totalMs":0}
                ]
                \"\"\");
        Assert.assertTrue(html.contains("timeline-card"), html);
        Assert.assertTrue(html.contains("ran"), html);
        Assert.assertFalse(html.contains("skipped"), html);
        Assert.assertEquals(count(html, "gantt-row gantt-lane\\""), 1, html);
>>>>>>> 025c20a (fix(report): skip tests without startedAtMs in timeline instead of hiding it)
    }"""
new="""    @Test
    public void skippedTestWithoutStartedAtMs_doesNotHideTimeline() throws Exception {
        String html = timeline(\"\"\"
                [
                  {"testId":"com.x.A.ran","thread":"pool-1-thread-1","status":"PASSED","totalMs":100,"startedAtMs":1000},
                  {"testId":"com.x.B.skipped","thread":"pool-1-thread-1","status":"SKIPPED","totalMs":0}
                ]
                \"\"\");
        Assert.assertTrue(html.contains("timeline-card"), html);
        Assert.assertTrue(html.contains("ran"), html);
        Assert.assertFalse(html.contains("skipped"), html);
        Assert.assertEquals(count(html, "gantt-row gantt-lane\\""), 1, html);
    }"""
if old in c:
    c2=c.replace(old,new)
    open(path,'w').write(c2)
    print('ok')
else:
    print('no')
