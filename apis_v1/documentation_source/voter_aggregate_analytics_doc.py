# apis_v1/documentation_source/voter_aggregate_analytics_doc.py
# Brought to you by We Vote. Be good.
# -*- coding: UTF-8 -*-


def voter_aggregate_analytics_doc_template_values(url_root):
    """
    Show documentation about voterAggregateAnalytics
    """
    required_query_parameter_list = [
        {
            'name':         'api_key',
            'value':        'string (from post, cookie, or get (in that order))',  # boolean, integer, long, string
            'description':  'The unique key provided to any organization using the WeVoteServer APIs',
        },
    ]

    optional_query_parameter_list = [
        {
            'name':         'google_civic_election_id',
            'value':        'integer',  # boolean, integer, long, string
            'description':  'Limit results to this election',
        },
        {
            'name':         'show_county_topics',
            'value':        'boolean',  # boolean, integer, long, string
            'description':  'Include statistics about topics followed by voters county-by-county.',
        },
        {
            'name':         'show_state_topics',
            'value':        'boolean',  # boolean, integer, long, string
            'description':  'Include statistics about topics followed by voters in each state.',
        },
        {
            'name':         'show_this_year_of_analytics',
            'value':        'integer',  # boolean, integer, long, string
            'description':  'Limit results to the analytics of this one year.',
        },
    ]

    potential_status_codes_list = [
    ]

    try_now_link_variables_dict = {
        # 'voter_device_id': '',
    }

    api_response = '{\n' \
                   '  "status": string,\n' \
                   '  "success": boolean,\n' \
                   '  "google_civic_election_id": integer ' \
                   '(if positive value, the unique election id we are focused on viewing. ' \
                   'If < 1,000,000 from google, if greater, generated by We Vote),\n' \
                   '  "voters": integer (the number of voters who used We Vote, limited by search parameters),\n' \
                   '  "voters_following_topics": integer (the number of voters following at least one topic),\n' \
                   '  "percent_of_voters_following_topics": integer (voters_following_topics / voters),\n' \
                   '  "year": integer (the year shown, default is "all years"),\n' \
                   '  "likely_left_from_issues": integer ' \
                   '(We Vote\'s estimate of the number of voters who lean politically left, ' \
                   'out of voters_following_topics. ' \
                   'See: calculate_likely_political_party_from_issues),\n' \
                   '  "likely_right_from_issues": integer,\n' \
                   '  "likely_democrat_from_issues": integer,\n' \
                   '  "likely_green_from_issues": integer,\n' \
                   '  "likely_libertarian_from_issues": integer,\n' \
                   '  "likely_republican_from_issues": integer,\n' \
                   '  "show_states_without_activity": boolean,\n' \
                   '  "show_state_topics": boolean,\n' \
                   '  "show_counties": boolean,\n' \
                   '  "show_counties_without_activity": boolean,\n' \
                   '  "show_county_topics": boolean,\n' \
                   '  "states": dict\n' \
                   '   {\n' \
                   '     "<STATE_CODE>": 2-digit string all-caps, key for dict,\n' \
                   '       {\n' \
                   '         "state_name": string,\n' \
                   '         "voters_in_state": integer (the number of voters who used We Vote in this state),\n' \
                   '         "voters_in_state_following_topics": integer ' \
                   '(# of voters in this state who chose 1+ topics),\n' \
                   '         "percent_voters_in_state_following_topics": string ' \
                   '(Percent of voters_in_state_following_topics divided by voters_in_state),\n' \
                   '         "counties": list of dicts (all counties that included activity)\n' \
                   '         [{\n' \
                   '           "county_name": string, (display name)\n' \
                   '           "county_short_name": string,\n' \
                   '           "county_fips_code": string,\n' \
                   '           "voters_in_county": integer (the number of voters who used We Vote in this county),\n' \
                   '           "voters_in_county_following": integer ' \
                   '(# of voters in this county who chose 1+ topics),\n' \
                   '           "percent_voters_in_county_following": integer ' \
                   '(voters_in_county_following / voters_in_county),\n' \
                   '           "topics_by_county": list (all topics in this county that included activity)\n' \
                   '           [{\n' \
                   '             "topic_name": string,\n' \
                   '             "issue_we_vote_id": string,\n' \
                   '             "voters_in_county_following_this_topic": integer ' \
                   '(# of voters in this county who followed this topic),\n' \
                   '             "percent_voters_in_county_following": string ' \
                   '(voters_in_county_following_this_topic / voters_in_county),\n' \
                   '             "percent_voters_in_county_following_active_only": ' \
                   '(voters_in_county_following_this_topic / voters_in_county_following),\n' \
                   '           }],\n' \
                   '         }],\n' \
                   '       },\n' \
                   '   },\n' \
                   '}'

    template_values = {
        'api_name': 'voterAggregateAnalytics',
        'api_slug': 'voterAggregateAnalytics',
        'api_introduction':
            "Retrieve the number of voters who have used We Vote. Many fields are not returned under some search "
            "configurations.",
        'try_now_link': 'apis_v1:voterAggregateAnalyticsView',
        'try_now_link_variables_dict': try_now_link_variables_dict,
        'url_root': url_root,
        'get_or_post': 'GET',
        'required_query_parameter_list': required_query_parameter_list,
        'optional_query_parameter_list': optional_query_parameter_list,
        'api_response': api_response,
        'api_response_notes':
            "",
        'potential_status_codes_list': potential_status_codes_list,
    }
    return template_values
