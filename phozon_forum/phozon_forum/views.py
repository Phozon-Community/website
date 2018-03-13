from django.http import Http404
from django.shortcuts import render

from phozon_forum import formatting

def forums(request):
	data = {
		"categories" : {
			0 : {
				"name" : "General",
				"html_safe_name" : formatting.html_safe("General"),
				"forums" : {
					0 : {
						"name" : "Announcements",
						"html_safe_name" : formatting.html_safe("Announcements"),
						"description" : "Announcements and other messages go here.",
						"post_count" : formatting.sexy_number(7),
						"last_reply" : {
							"thread_id" : 0,
							"thread_name" : "This website is bad",
							"author_id" : 0,
							"author_name" : "TheBigGey",
							"post_date" :  "10 Hours Ago"
						},
						"sub_forums" : {
							0 : {
								"name" : "News",
								"html_safe_name" : formatting.html_safe("News"),
								"description" : "Irrelevant Nonsense"
							}
						}
					},
					1 : {
						"name" : "General Discussion",
						"html_safe_name" : formatting.html_safe("General Discussion"),
						"description" : "Talk about generic boring stuff here.",
						"post_count" : formatting.sexy_number(12314),
						"last_reply" : {
							"thread_id" : 1,
							"thread_name" : "Am I the Big Gey?",
							"author_id" : 1,
							"author_name" : "Adam",
							"post_date" :  "Just Now"
						},
						"sub_forums" : {}
					},
				}
			},
			1 : {
			 	"name" : "Help & Support",
			 	"html_safe_name" : formatting.html_safe("Help & Support"),
			 	"forums" : {
					0 : {
						"name" : "Technical Support",
						"html_safe_name" : formatting.html_safe("Technical Support"),
						"description" : "Go for help here if you accidentally uninstall your GPU drivers.",
						"post_count" : formatting.sexy_number(1),
						"last_reply" : {
							"thread_id" : 2,
							"thread_name" : "Halp I uninstall GPU drivers.",
							"author_id" : 2,
							"author_name" : "Stafford",
							"post_date" :  "4 Years Ago"
						},
						"sub_forums" : {
							0 : {
								"name" : "Solved",
								"html_safe_name" : formatting.html_safe("Solved"),
								"description" : "We always delete answers."
							},
							1 : {
								"name" : "Unsolved",
								"html_safe_name" : formatting.html_safe("Unsolved"),
								"description" : "Problems too hard for anyone."
							}
						}
					}
				}
			}
		}
	}
	web_renderer = render(
		request, 
		'main.html',
		{
			'pageTemplate': 'forums/forums.html',
			'data': data
		}
	)

	return web_renderer