#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
from sonarqube import SonarQubeClient

if __name__ == "__main__":
    url = 'http://localhost:9000'
    username = "admin"
    password = "admin"
    sonar = SonarQubeClient(sonarqube_url=url, username=username, password=password)

    """ Search for issues """
    issues1 = sonar.issues.search_issues(componentKeys="my_project", branch="develop")
    # or
    issues2 = sonar.issues.search_issues(componentKeys="my_project", resolutions="WONTFIX")

    """ Assign/Unassign an issue """
    sonar.issues.issue_assign(issue="AXQp_hOWOhAXidGT7-d7", assignee="jialiang.shi")

    """ Change severity """
    sonar.issues.issue_change_severity(issue="AXQp_hOWOhAXidGT7-d7", severity="BLOCKER")

    """ Change type of issue, for instance from 'code smell' to 'bug' """
    sonar.issues.issue_set_type(issue="AXQp_hOWOhAXidGT7-d7", issue_type="CODE_SMELL")

    """ Add a comment """
    sonar.issues.issue_add_comment(issue="AXQp_hOWOhAXidGT7-d7", text="this is a import bug, must need be fixed.")

    """ Delete a comment """
    sonar.issues.issue_delete_comment(comment="AXQp_hOWOhAXidGT7-d7")

    """ Edit a comment """
    sonar.issues.issue_edit_comment(comment="AU-Tpxb--iU5OvuD2FLy",
                                    text="Won't fix because it doesn't apply to the context")

    """ Do workflow transition on an issue """
    sonar.issues.issue_do_transition(issue="AXQp_hOWOhAXidGT7-d7", transition="wontfix")

    """ Search SCM accounts which match a given query """
    accounts = sonar.issues.search_scm_accounts("my_project")

    """ Bulk change on issues """
    sonar.issues.issues_bulk_change(issues="AXQp_hOWOhAXidGT7-d7", remove_tags="security")
    # or
    sonar.issues.issues_bulk_change(issues="AXQp_hOWOhAXidGT7-d7", do_transition="falsepositive")
    # or
    sonar.issues.issues_bulk_change(issues="AXQp_hOWOhAXidGT7-d7", issue_type="VULNERABILITY")

    """ Display changelog of an issue """
    changelog = sonar.issues.get_issue_changelog(issue="AXQp_hOWOhAXidGT7-d7")

    """ Set tags on an issue """
    sonar.issues.issue_set_tags(issue="AXQp_hOWOhAXidGT7-d7", tags="security,cwe,misra-c")

    """ List tags """
    tags = sonar.issues.get_issues_tags(project="my_project")
