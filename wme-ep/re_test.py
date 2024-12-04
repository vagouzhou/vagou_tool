import re
text = '''
"Hi, Wallice Tyler EP request for MC client 13.8.0

PR link: https://sqbu-github.cisco.com/WebExSquared/wme/pull/21006
JIRAs: https://jira-eng-gpk2.cisco.com/jira/browse/WEBEX-335916

1. Which of the below categories does you PR fall under?
BugID: WEBEX-335916

2. Explain why this can't wait until the next GA.
This issue happened at some company's all-hands meetings recently, one of the customers request us to fix it as soon as possible.

3. Is this a regression from the current shipping product?
Not a regression

4. How many users are impacted by this issue?
Recently at least three customers reported this issue, In fact, this problem has always been a probability

5. Explain why this is a low risk change?
The change was covered by a feature toggle and we had do some testing based on master branch for MC

6. Which component(s) and client type are impacted?
MC client

7. How do you plan to avoid this issue from happening again late in our release process?
1). add related metrics to calculate the percentage that might have this problem, observe the statics distribution
2}. design more better algorithm data structure to cover this kind of case on UCF"
'''

# Extract details using regex

jira_id = re.search(r'https://jira-eng-gpk2\.cisco\.com/jira/browse/(WEBEX|SPARK)-\d+', text)
if jira_id is None:
    jira_id = re.search(r'\[(WEBEX|SPARK)-\d+\]', text)
jira_id = jira_id.group(0).strip() if jira_id else None
pr_link = re.search(r'https://sqbu-github\.cisco\.com/WebExSquared/wme/pull/\d+', text)
if pr_link is None:
    pr_link = re.search(r'https://sqbu-github\.cisco\.com/WebexApps/webex-apps/pull/\d+', text)
pr_link = pr_link.group(0).strip() if pr_link else None
title = re.search(r'Title:(.*?)\n', text, re.DOTALL)
title = title.group(1).strip() if title else None

print(jira_id if jira_id else 'jira_id Not Found')
print(pr_link if pr_link else 'pr_link Not Found')
print(title if title else 'title Not Found')