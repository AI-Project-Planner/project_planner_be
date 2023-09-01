# project_planner_be

## About Project Planner
Project Planner is designed to streamline the project planning process for junior to mid level developers. By leveraging advanced AI technology, this app assists users in crafting comprehensive project plans and generating innovative ideas tailored to their chosen project type and preferred technologies.

[Project Spec/Requirements](https://mod4.turing.edu/projects/capstone/)

### Deployed UI
- [Frontend Deployment]()
- [Frontend Repository](https://github.com/AI-Project-Planner/project-planner-ui)

## Table of Contents
- RESTful Endpoints
- Environment Set Up
- Contributors

## RESTful Endpoints
<details close>

### Generate a Project
<details close>

```http
POST /api/v1/users/:id/projects
```

#### Parameters:

```
:id => user_id
```

| Code | Description |
| :--- | :---------- |
| 200  | `OK`        |

#### Request Body:

```json
{
	"type": "frontend",
	"technologies": "react, typescript and javascript",
	"time": "1 week",
	"collaborators": 2
}
```

#### Example Response:

```json
{
	"id": "1",
	"type": "project",
	"attributes": {
		"name": "TaskMaster Pro",
		"steps": "Project Setup: Create Git repository and define project structure\nBackend Setup: Develop Express.js application, set up API routes\nDatabase Design: Design and implement database schema",
		"description": "TaskMaster Pro is an all-inclusive task management application designed to optimize team collaboration and productivity.",
	  "features": "User registration and login\nCreate, assign, update, and track tasks\nReal-time collaboration and updates\nPriority-based task categorization",
		"interactions": "User logs in to TaskMaster Pro account.\nDashboard displays tasks by priority: High, Medium, Low.\nUser adds a task, assigns it, and sets a due date.\nTask appears under the respective priority category.\nAssigned user starts task, status updates in real-time.\nUpon completion, task is marked as done and updates for all.",
		"colors": "#3498DB\n#27AE60\n#F39C12\n#F0F3F4\n#333333\n#E74C3C",
		"saved": false,
		"timeline": "week",
    "timeline_int": 1,
		"user_id": "1"
	}
}
```

Error Response:

| Code | Description |
| :--- | :---------- |
| 503  | `Server is down.` |

```json
	{
		"Error": "Server is down.",
		"Status": 500
	}
```

</details>

### Update Saved Status for A Users Project

<details close>

```http
PATCH /api/v1/users/:user_id/projects/:project_id/
```

#### Parameters:

```
:user_id => user_id
:project_id => project_id
```

| Code | Description |
| :--- | :---------- |
| 202  | `ACCEPTED`        |

#### Request Body:

```json
{
	"saved": "true"
}
```

#### Example Response:

```json
{
	"id": "1",
	"type": "project",
	"attributes": {
		"name": "TaskMaster Pro",
		"steps": "Project Setup: Create Git repository and define project structure\nBackend Setup: Develop Express.js application, set up API routes\nDatabase Design: Design and implement database schema",
		"description": "TaskMaster Pro is an all-inclusive task management application designed to optimize team collaboration and productivity.",
	  "features": "User registration and login\nCreate, assign, update, and track tasks\nReal-time collaboration and updates\nPriority-based task categorization",
		"interactions": "User logs in to TaskMaster Pro account.\nDashboard displays tasks by priority: High, Medium, Low.\nUser adds a task, assigns it, and sets a due date.\nTask appears under the respective priority category.\nAssigned user starts task, status updates in real-time.\nUpon completion, task is marked as done and updates for all.",
		"colors": "#3498DB\n#27AE60\n#F39C12\n#F0F3F4\n#333333\n#E74C3C",
		"saved": true,
		"timeline": "week",
    "timeline_int": 1,
		"user_id": "1"
	}
}
```

Error Response:

| Code | Description |
| :--- | :---------- |
| 404  | `Project or User ID not found.` |

```json
	{
		"Error": "Project or User ID not found.",
		"Status": 404
	}
```

</details>

### Get ALL of a Users Projects

<details close>

```http
GET /api/v1/users/:id/projects/
```

#### Parameters:

```
:id => user_id
```

| Code | Description |
| :--- | :---------- |
| 200  | `OK`        |


#### Example Response:

```json
{
  "data": 
  [
    {
      "id": "1",
      "type": "project",
      "attributes": {
        "name": "TaskMaster Pro",
        "steps": "Project Setup: Create Git repository and define project structure\nBackend Setup: Develop Express.js application, set up API routes\nDatabase Design: Design and implement database schema",
        "description": "TaskMaster Pro is an all-inclusive task management application designed to optimize team collaboration and productivity.",
        "features": "User registration and login\nCreate, assign, update, and track tasks\nReal-time collaboration and updates\nPriority-based task categorization",
        "interactions": "User logs in to TaskMaster Pro account.\nDashboard displays tasks by priority: High, Medium, Low.\nUser adds a task, assigns it, and sets a due date.\nTask appears under the respective priority category.\nAssigned user starts task, status updates in real-time.\nUpon completion, task is marked as done and updates for all.",
        "colors": "#3498DB\n#27AE60\n#F39C12\n#F0F3F4\n#333333\n#E74C3C",
        "saved": true,
        "timeline": "week",
        "timeline_int": 1,
        "user_id": "1"
      }
    },
    {
      "id": "2",
      "type": "project",
      "attributes": {
        "name": "Different Project Pro",
        "steps": "Project Setup: Create Git repository and define project structure\nBackend Setup: Develop Express.js application, set up API routes\nDatabase Design: Design and implement database schema",
        "description": "It's different!",
        "features": "User registration and login\nCreate, assign, update, and track tasks\nReal-time collaboration and updates\nPriority-based task categorization",
        "interactions": "User logs in to TaskMaster Pro account.\nDashboard displays tasks by priority: High, Medium, Low.\nUser adds a task, assigns it, and sets a due date.\nTask appears under the respective priority category.\nAssigned user starts task, status updates in real-time.\nUpon completion, task is marked as done and updates for all.",
        "colors": "#3498DB\n#27AE60\n#F39C12\n#F0F3F4\n#333333\n#E74C3C",
        "saved": true,
        "timeline": "days",
        "timeline_int": 4,
        "user_id": "1"
      }
    }
  ]
}
```

Error Response:

| Code | Description |
| :--- | :---------- |
| 404  | `User ID not found.` |

```json
	{
		"Error": "User ID not found.",
		"Status": 404
	}
```

</details>
</details>

## Environment Set-Up

### Prerequisites

Before getting started, ensure that you have the following installed on your system:

- Python (version 3.11.5 or higher)
- pip (Python package manager)

### Installation

Follow these steps to install the Project Planner App:

1. Clone the repository:

```
git clone https://github.com/AI-Project-Planner/project_planner_be.git
```

2. Navigate to the project directory:

```
cd project_planner_be
```

3. Create a virtual environment (optional but recommended):

```
python3 -m venv env
```

4. Activate the virtual environment:

macOS/Linux:

```
source env/bin/activate
```

Windows:

```
source env/Scripts/activate
```

5. Install the required environment packages:

```
pip install -r requirements.txt
```

6. Run migrations:

```
python3 manage.py makemigrations
python3 manage.py migrate
```

7. Run test suite to ensure functionality is working.

```
python3 manage.py test
```

If any modules are missing:

<details close>

```
pip install < MISSING MODULE >
```
</details>
</br>
</br>

7. Start the development server:

```
python3 manage.py runserver
```

The server should start running at http://127.0.0.1:8000/. 

## Contributors

- Amy Marie Spears
  - [LinkedIn](https://www.linkedin.com/in/amy-marie-spears-900997105/)
  - [GitHub](https://github.com/amspears007)
- Javen Wilson
  - [LinkedIn](https://www.linkedin.com/in/javen-wilson/)
  - [GitHub](https://github.com/javenb022)
- Garrett Gregor
  - [LinkedIn](https://www.linkedin.com/in/garrett-gregor/)
  - [GitHub](https://github.com/garrettgregor)
- Michael Callahan
  - [LinkedIn](https://www.linkedin.com/in/michaelcallahanjr/)
  - [GitHub](https://github.com/calforcal)