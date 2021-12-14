from pyvotal_tracker import PivotalTrackerAPI

def main():
    # QUICK MASSIVE TEST METHOD
    token = 'MY_TOKEN'
    project_id = 'MY_PROJECT_ID'
    timestamp = '2021-12-01T00:00:00Z'
    pt = PivotalTrackerAPI(token)
    my_account = pt.get_my_account() 
    # accounts = pt.get_accounts()
    # account_id = str(accounts[0]['id'])
    # account = pt.get_account(account_id).
    # my_people = pt.get_my_people(project_id)
    # person_id = my_people[0]['person']['id']
    # my_notifications = pt.get_my_notifications(timestamp)
    # people_notifications = pt.get_people_notifications(person_id, timestamp)
    # projects = pt.get_projects(account_id)
    # account_membership = pt.get_account_membership(account_id,person_id)
    # project = pt.get_project(project_id)
    # project_iterations = pt.get_project_iterations(project_id)
    # project_labels = pt.get_project_labels(project_id) 
    # label = project_labels[0]['name']
    # stories = pt.get_stories(project_id,None,'kb1', 'unstarted',timestamp) 
    # if len(stories) :
    #   story_id = stories[0]['id']    
    #   story = pt.get_story(story_id, project_id) 
    #   story_comments = pt.get_story_comments(story_id, project_id) 
    #   if len(story_comments) :
    #     comment_id = story_comments[0]['id']
    #     story_comment = pt.get_story_comment(story_id, project_id, comment_id) 
    #   story_owners = pt.get_story_owners(story_id, project_id) 
    #   story_tasks = pt.get_story_tasks(story_id, project_id) 
    #   if len(story_tasks) :
    #     task_id = story_tasks[0]['id']
    #     story_task = pt.get_story_task(story_id, project_id, task_id) 

    # account_summaries = pt.get_account_summaries() 
    # account_memberships = pt.get_account_memberships(account_id)
    # iterations = pt.get_iterations(project_id) 
    # project_activity = pt.get_project_activity(project_id) 
    # project_epics = pt.get_project_epics(project_id) 
    # epic_id = project_epics[0]['id']
    # project_epic = pt.get_project_epic(project_id, epic_id) 
    # project_epic_comments = pt.get_project_epic_comments(project_id, epic_id) 
    # if len(project_epic_comments) :
    #   comment_id = project_epic_comments[0]['id']
    #   project_epic_comment = pt.get_project_epic_comment(project_id, epic_id, comment_id) 
    # epic = pt.get_epic(epic_id)     
    
    # project_memberships = pt.get_project_memberships(project_id) 
    # membership_id = project_memberships[0]['id']
    # project_membership = pt.get_project_membership(membership_id,project_id)

if __name__ == '__main__':
    main()