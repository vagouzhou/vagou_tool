import pandas as pd
from wme_ep import extract_details
items = [
    {
        'id': 'Y2lzY29zcGFyazovL3VzL01FU1NBR0UvMDRkNzAwZjAtYjBhMC0xMWVmLWI3Y2EtMDdhNDUxM2RiYmUw',
        'roomId': 'Y2lzY29zcGFyazovL3VzL1JPT00vM2I1ZDY5YzAtODA1My0xMWVhLTk2OTYtNTE0MzQ3ODc2NjZj',
        'roomType': 'group',
        'text': '''
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

''',
        'personId': 'Y2lzY29zcGFyazovL3VzL1BFT1BMRS80YmEzMTg1Mi0yNjljLTQ4YzEtYmNlYS1iN2I2YzA5OGEyYTY',
        'personEmail': 'xinxzhen@cisco.com',
        'created': '2024-12-02T11:24:39.423Z',
        'parentId': 'Y2lzY29zcGFyazovL3VzL01FU1NBR0UvNTU5ODhhYjAtYWY4Yi0xMWVmLTljOTQtNzU2MmU2M2JkZTUz',
        'html': '<p>Thx</p>',
        'mentionedPeople': [],
        'files': [],
        'updated': '2024-12-02T12:00:00.000Z'
    }
]

extract_details = extract_details(items[0])
pd.set_option('display.max_colwidth', 150)  # Set the max column width to None to display all content
print(extract_details)