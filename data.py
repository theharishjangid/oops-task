user_data = [{
		"id": 1,
		"name": "ab1",
		"pass": "wevfhevfew1",
		"role": "subscriber",
        "desc": "asfbrebgher g  shfdeh"
	},
	{
		"id": 2,
		"name": "abc2",
		"pass": "wevfhevfew2",
		"role": "subscriber",
        "desc": "asfbrebgher g  shfdeh"
	},
	{
		"id": 3,
		"name": "abc3",
		"pass": "wevfhevfew3",
		"role": "subscriber",
        "desc": "asfbrebgher g  shfdeh"
	},
	{
		"id": 4,
		"name": "abc4",
		"pass": "wevfhevfew4",
		"role": "admin",
        "desc": "asfbrebgher g  shfdeh"
	},
	{
		"id": 5,
		"name": "abc5",
		"pass": "wevfhevfew5",
		"role": "subscriber",
        "desc": "asfbrebgher g  shfdeh"
	},
	{
		"id": 6,
		"name": "abc6",
		"pass": "wevfhevfew6",
		"role": "subscriber",
        "desc": "asfbrebgher g  shfdeh"
	},
	{
		"id": 7,
		"name": "abc7",
		"pass": "wevfhevfew7",
		"role": "moderator",
        "desc": "asfbrebgher g  shfdeh"
	},
	{
		"id": 8,
		"name": "abc8",
		"pass": "wevfhevfew8",
		"role": "subscriber",
        "desc": "asfbrebgher g  shfdeh"
	},
	{
		"id": 9,
		"name": "abc9",
		"pass": "wevfhevfew9",
		"role": "subscriber",
        "desc": "asfbrebgher g  shfdeh"
	},
	{
		"id": 10,
		"name": "abc10",
		"pass": "wevfhevfew10",
		"role": "moderator",
        "desc": "asfbrebgher g  shfdeh"
	}
]

ROLES = {
	"role_priviledges": {
		"admin": {
			"allowed": ["all"]
		},
		"moderator": {
			"allowed": ["set_user_role", "edit_user", "get_user_info", "user_count", "role_based_user_count", "get_user_role"],
			"not_allowed": ["delete_user", "add_user"]
		},
		"subscriber": {
			"allowed": ["get_user_info", "user_count", "role_based_user_count", "get_user_role"],
			"not_allowed": ["set_user_role", "edit_user", "delete_user", "add_user"]
		}
	}
}