import rest_methods

'''
Based on  https://www.pivotaltracker.com/help/api?version=v5#top
Constructor arguments:
    token: String. API token for v5 API. https://www.pivotaltracker.com/help/api#top
'''

class PivotalTrackerAPI():
    """Only implemented GET methods of Pivotal Tracker."""

    def __init__(self, token, get_projects=False):
        """Requires a valid PivotalTracker token to init the class"""
        if not token:
            raise Exception('No API token received or bad value')
        self.version = 5
        self.token = token
        self.pivotal_url = 'https://www.pivotaltracker.com/services/v5/'
        # self.projects = None
        # if get_projects:
        #     self.projects()

    # endpoint /me
    def get_my_account(self) : 
        url =  '/me'
        # TODO : consult and add optional search parameters to refine the results
        return self.request(url, 'GET')

    # endpoint /me/people
    def get_my_people(self, project_id, filter_by = None, limit = 10, offset = 0) :
        url =  '/my/people?project_id=' + str(project_id)

        params = []
        if type(filter_by) == str:
            params.append("filter_by="+filter_by)
        if len(params) > 0 :
            url += '?'+'&'.join(params)

        # TODO : consult and add optional search parameters to refine the results
        return self.request(url, 'GET',limit, offset)

    # endpoint /my/notifications
    def get_my_notifications(self, created_after = None, updated_after = None, notification_types = None, limit = 20) :
        url =  '/my/notifications'
        if type(created_after) == str and type(updated_after) == str:
            return 'cannot have both parameters'
        params = []
        if type(created_after) == str and not updated_after:
            params.append("created_after="+created_after)
        if not created_after and type(updated_after) == str:
            params.append("updated_after="+updated_after)
        if type(notification_types) == str:
            params.append("notification_types="+notification_types)
        if len(params) > 0 :
            url += '?'+'&'.join(params)
        # TODO : consult and add optional search parameters to refine the results
        return self.request(url, 'GET', limit)
    
    # endpoint /people/{person_id}/notifications/since/{timestamp}
    def get_people_notifications(self, person_id, timestamp, notification_types = None, limit = 10) :
        url =  '/people/' + str(person_id) + '/notifications/since/' + str(timestamp)

        params = []
        if type(notification_types) == str:
            params.append("notification_types="+notification_types)
        if len(params) > 0 :
            url += '?'+'&'.join(params)
        
        # TODO : consult and add optional search parameters to refine the results
        return self.request(url, 'GET', limit)

    # endpoint /projects
    def get_projects(self,account_ids = None) :
        url = 'projects'
        
        params = []
        if type(account_ids) == str:
            params.append("account_ids="+account_ids)
        if len(params) > 0 :
            url += '?'+'&'.join(params)
        
        # TODO : consult and add optional search parameters to refine the results
        return self.request(url, 'GET')

    # endpoint /projects/{project_id}
    def get_project(self,project_id = None) :
        url = 'projects/' + str(project_id)
        # TODO : consult and add optional search parameters to refine the results
        return self.request(url, 'GET')

    # endpoint /projects/{project_id}/iterations
    def get_project_iterations(self,project_id = None,label = None,scope = None,limit = 10,offset = 0) :
        url = 'projects/' + str(project_id)
        
        params = []
        if type(label) == str:
            params.append("label="+label)
        if type(scope) == str:
            params.append("scope="+scope)
        if len(params) > 0 :
            url += '?'+'&'.join(params)
        
        # TODO : consult and add optional search parameters to refine the results
        return self.request(url, 'GET',limit,offset)

    # endpoint /projects/{project_id}/stories/{story_id}
    def get_story(self, story_id, project_id) : 
        url = 'projects/' + str(project_id) + '/stories/' + str(story_id)
        
        params = []
        if type(filter) == str:
            params.append("filter=" + filter)
        
        if len(params) > 0 :
            url += '?'+'&'.join(params)
        
        # TODO : consult and add optional search parameters to refine the results
        return self.request(url, 'GET')

    # endpoint /projects/{project_id}/stories with filters
    def get_stories(self,project_id,filter = None,labels = None, state = None,updated_after = None) : 
        url = "projects/" + str(project_id)+"/stories"

        params = []
        if type(filter) == str:
            params.append("filter=" + filter)
        if type(labels) == str:
            params.append("with_label=" + labels)
        if type(state) == str:
            params.append("with_state=" + state)
        if type(updated_after) == str:
            params.append("updated_after="+updated_after)

        if len(params) > 0 :
            url += '?'+'&'.join(params)        

        # TODO : consult and add optional search parameters to refine the results
        return self.request(url, 'GET')

    # endpoint /accounts/{account_id}
    def get_account(self,account_id) : 
        url = 'accounts/' + str(account_id)
        # TODO : consult and add optional search parameters to refine the results
        return self.request(url, 'GET')

    # endpoint /accounts
    def get_accounts(self) : 
        url = 'accounts'
        # TODO : consult and add optional search parameters to refine the results
        return self.request(url, 'GET')

    # endpoint /account_summaries
    def get_account_summaries(self) : 
        url = 'account_summaries'
        # TODO : consult and add optional search parameters to refine the results
        return self.request(url, 'GET')

    # endpoint /accounts/{account_id}/memberships/{person_id}
    def get_account_membership(self,account_id,person_id) :
        url = 'accounts/' + str(account_id) + '/memberships/' + str(person_id)
        # TODO : consult and add optional search parameters to refine the results
        return self.request(url, 'GET')

    # endpoint /projects/{project_id}/memberships/{membership_id}
    def get_project_membership(self,membership_id,project_id) :
        url = 'projects/' + str(project_id) + '/memberships/' + str(membership_id)
        # TODO : consult and add optional search parameters to refine the results
        return self.request(url, 'GET')

    # endpoint /accounts/{account_id}/memberships
    def get_account_memberships(self,account_id) :
        url = 'accounts/' + str(account_id) + '/memberships'
        # TODO : consult and add optional search parameters to refine the results
        return self.request(url, 'GET')

    # endpoint /epics/{epic_id}
    def get_epic(self, epic_id) : 
        url = 'epics/' + str(epic_id)
        # TODO : consult and add optional search parameters to refine the results
        return self.request(url, 'GET')

    # endpoint /projects/{project_id}/iterations
    def get_iterations(self, project_id, limit=10, offset=0) : 
        url = 'projects/' + str(project_id) + '/iterations'
        # TODO : consult and add optional search parameters to refine the results
        return self.request(url,'GET',limit,offset)

	# endpoint /projects/{project_id}/activity
    def get_project_activity(self,project_id, limit=50) : 
        url = 'projects/'+str(project_id)+'/activity'
        # TODO : consult and add optional search parameters to refine the results
        return self.request(url,'GET',limit)

    # endpoint /projects/{project_id}/epics/{epic_id}
    def get_project_epic(self, project_id, epic_id) : 
        url = 'projects/' + str(project_id) + '/epics/' + str(epic_id)
        # TODO : consult and add optional search parameters to refine the results
        return self.request(url, 'GET')

    # endpoint /projects/{project_id}/stories/{story_id}/comments
    def get_project_epic_comments(self, project_id, epic_id) : 
        url = 'projects/' + str(project_id) + '/epics/' + str(epic_id) + '/comments'
        # TODO : consult and add optional search parameters to refine the results
        return self.request(url, 'GET')

    # endpoint /projects/{project_id}/stories/{story_id}/comments/{comment_id}
    def get_project_epic_comment(self, project_id, epic_id, comment_id) : 
        url = 'projects/' + str(project_id) + '/epics/' + str(epic_id) + '/comments/' + str(comment_id)
        # TODO : consult and add optional search parameters to refine the results
        return self.request(url, 'GET')

    # endpoint /projects/{project_id}/epics
    def get_project_epics(self, project_id) : 
        url = 'projects/' + str(project_id) + '/epics'
        # TODO : consult and add optional search parameters to refine the results
        return self.request(url, 'GET')

    # endpoint /projects/{project_id}/labels
    def get_project_labels(self, project_id) : 
        url = 'projects/' + str(project_id) + '/labels'
        # TODO : consult and add optional search parameters to refine the results
        return self.request(url, 'GET')

    # endpoint /projects/{project_id}/memberships
    def get_project_memberships(self, project_id) : 
        url = 'projects/' + str(project_id) + '/memberships'
        # TODO : consult and add optional search parameters to refine the results
        return self.request(url, 'GET')

    # endpoint /projects/{project_id}/stories/{story_id}/comments/{comment_id}
    def get_story_comment(self, story_id, project_id, comment_id) : 
        url = 'projects/' + str(project_id) + '/stories/' + str(story_id) + '/comments/' + str(comment_id)
        # TODO : consult and add optional search parameters to refine the results
        return self.request(url, 'GET')

    # endpoint /projects/{project_id}/stories/{story_id}/comments
    def get_story_comments(self, story_id, project_id) : 
        url = 'projects/' + str(project_id) + '/stories/' + str(story_id) + '/comments'
        # TODO : consult and add optional search parameters to refine the results
        return self.request(url, 'GET')

    # endpoint /projects/{project_id}/stories/{story_id}/owners
    def get_story_owners(self, story_id, project_id) : 
        url = 'projects/' + str(project_id) + '/stories/' + str(story_id) + '/owners'
        # TODO : consult and add optional search parameters to refine the results
        return self.request(url, 'GET')

    # endpoint /projects/{project_id}/stories/{story_id}/tasks
    def get_story_tasks(self, story_id, project_id) : 
        url = 'projects/' + str(project_id) + '/stories/' + str(story_id) + '/tasks'
        # TODO : consult and add optional search parameters to refine the results
        return self.request(url, 'GET')

    # endpoint /projects/{project_id}/stories/{story_id}/tasks/{task_id}
    def get_story_task(self, story_id, project_id, task_id) : 
        url = 'projects/' + str(project_id) + '/stories/' + str(story_id) + '/tasks/' + str(task_id)
        # TODO : consult and add optional search parameters to refine the results
        return self.request(url, 'GET')

    # request method (call to rest_calls script)
    def request(self,url, http_method = 'GET',limit = 10, offset = 0) :
        result = str(http_method) + " has not been implemented yet"
        if http_method == 'GET' :
            query_data = None
            if type(limit) == int and type(limit) == offset :
                query_data = query_data={'limit': limit, 'offset': offset} 
            result = rest_methods.get(self.pivotal_url + url, query_data, headers={'X-TrackerToken': self.token}, return_json=True)            
        
        return result