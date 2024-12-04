import re
text = '''
"Hi Wallice Tyler
EP request for 44.12:
Jira: https://jira-eng-gpk2.cisco.com/jira/browse/SPARK-587390
Title: IOS client joining meeting with music mode, then change to noise removal, noise removal can't work
PR: https://sqbu-github.cisco.com/WebExSquared/wme/pull/22902
1.Which of the below category does your PR fall under? (Toggles/ telemetry/ bugs(S?, P?))
bug(S2,P2).
2.Explain why this can't wait until next GA.
This bug cause noise removal can’t work in iOS if joining meeting with music mode, which is a bug in S2 and needs to be fixed as soon as possible. 
3. Is this a regression from current shipping product? 
Yes. 
4. How many users are impacted by this issue? 
iOS users. 
5.Explain why this is a low risk change? 
Just small code change and already fully verified in different platforms. 
6.Which component(s) and clients type are impacted? 
All 
5. How do you plan to avoid this issue from happening again late in our release process? 
1.Add TA for test the effect of different audio mode joining meeting and audio mode change. 
2.Self-testing should cover more platforms and possible scenarios. 
Please give it a review. Thanks "
'''

jira_id = re.search(r'Jira: (.*?)\n', text, re.DOTALL)
pr_link = re.search(r'PR: (.*?)\n', text, re.DOTALL)
title = re.search(r'Title: (.*?)\n', text, re.DOTALL)
#ep_category = re.search(r'Which of the below category.*\n\s*(.*?)\n2\.', text, re.DOTALL)
ep_category = re.search(r'Which of the below category does your PR fall under\?.*?\n\s*(.*?)\n', text, re.DOTALL)
why_need_ep = re.search(r'Explain why this can\'t wait until next GA\.\n(.*?)\n3\.', text, re.DOTALL)
is_regression = re.search(r'Is this a regression from current shipping product\?\n(.*?)\n4\.', text, re.DOTALL)
#Is this a regression from current shipping product\?\n(.*?)\n4\.
#Is this a regression from current shipping product\?\s*\n\s*(.*?)\s*\n\s*4\.
issue_impact = re.search(r'How many users are impacted by this issue\?\n(.*?)\n5\.', text, re.DOTALL)
risk = re.search(r'Explain why this is a low risk change\?\n(.*?)\n6\.', text, re.DOTALL)
issue_scope = re.search(r'Which component\(s\) and clients type are impacted.*\n(.*?)\n(.*?)\n7\.', text, re.DOTALL)
what_improve = re.search(r'How do you plan to avoid this issue from happening again late in our release process\?\n(.*?)\nPlease', text, re.DOTALL)


print(jira_id.group(1).strip() if jira_id else 'jira_id Not Found')
print(pr_link.group(1).strip() if pr_link else 'pr_link Not Found')
print(title.group(1).strip() if title else 'title Not Found')
print(ep_category.group(1).strip() if ep_category else 'ep_category Not Found')
print(why_need_ep.group(1).strip() if why_need_ep else 'why_need_ep Not Found')
print(is_regression.group(1).strip() if is_regression else 'is_regression Not Found')
print(issue_impact.group(1).strip() if issue_impact else 'issue_impact Not Found')
print(risk.group(1).strip() if risk else 'risk Not Found')
print(issue_scope.group(1).strip() if issue_scope else 'issue_scope Not Found')
print(what_improve.group(1).strip() if what_improve else 'what_improve Not Found')