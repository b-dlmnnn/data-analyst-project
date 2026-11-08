# SMART TASK MANAGER (AKILLI GÖREV YÖNETİCİSİ)

#### Video URL: https://youtu.be

#### Description:
Welcome to the Smart Task Manager project documentation. This application is a fully comprehensive, terminal-based to-do list and task tracking solution built natively with Python 3 and powered by an optimized SQLite3 relational database backend. It has been carefully designed and meticulously developed as the culmination of the CS50x Introduction to Computer Science course to demonstrate proficiency in software design patterns, structured query language, defensive programming, automated unit testing methodologies, and intuitive command-line interface design.

## Project Overview and Core Purpose
In the modern digital age, tracking daily tasks and maintaining organized workflows is paramount to achieving high personal productivity and enterprise efficiency. While complex graphical applications exist, they often suffer from significant system resource overhead, distracting visual clutter, and lack of integration with developer workflows. The Smart Task Manager addresses these shortcomings by providing a lightning-fast, minimalist, and highly reliable environment engineered directly for the terminal. By storing information inside a structured SQL dataset, the application ensures that no matter when or how the user exits the system, their critical records are persistently saved with complete transactional integrity.

## Detailed Architectural Components

### 1. Relational Database Architecture (`init_db`)
The foundational backbone of the application relies heavily on robust relational data constraints. When the program initialises via the `init_db()` function, it verifies the physical presence of the local binary file titled `todo.db`. If this database file does not exist within the execution environment directory, the application programmatically spins up a connection and generates a clean schema. The underlying table structured as `tasks` contains carefully configured columns:
- `id`: Configured as an `INTEGER PRIMARY KEY AUTOINCREMENT` field to uniquely identify records and guarantee sequential referencing.
- `title`: An absolute `TEXT NOT NULL` constraint field storing the clear alphanumeric name of the registered chore.
- `status`: Designed as a flexible string parameter with a `DEFAULT 'Bekliyor'` constraint, indicating whether the task lifecycle is currently pending or completely resolved.

### 2. Defensive Task Creation Lifecycle (`add_task`)
The functionality responsible for expanding the user dataset is engineered defensively against invalid user inputs. The `add_task(title)` process opens an isolated connection to the SQLite stack, prepares a secure paramterized dynamic query string, and inserts the user input securely. Parameterization ensures complete mitigation of data corruption or prompt manipulation. It automatically prints a success message upon execution, confirming to the user that their data has transitioned properly into persistent system storage.

### 3. Visual Representation Layer (`list_tasks`)
The visualization of tasks is implemented through structured tabular formatting inside the terminal. The `list_tasks()` engine extracts records via custom structured selection queries. It maps dataset values dynamically into highly expressive visual cues: completed tasks display a vibrant tick mark symbol (`✔`), whereas pending tasks feature a distinct cross symbol (`❌`). If the retrieved data array returns empty, the function gracefully handles the condition by warning the user that no items are present, instead of breaking the terminal presentation layer.

### 4. Record Modification Processes (`complete_task` & `delete_task`)
Modifying or purging records requires precision targeting to prevent unintended operations on nearby indices. Both procedures demand explicit primary key arguments from the runtime loop. The `complete_task(task_id)` changes the status parameter dynamically to 'Tamamlandı'. The `delete_task(task_id)` completely drops the matching entity row from the table structure. Utilizing native cursor rowcount tracking metrics, the program detects if an invalid integer was queried, gracefully feeding back clear failure notifications to the screen without causing logical code execution halts.

### 5. Automated Validation Framework (`test_project.py`)
To fulfill strict continuous software delivery paradigms, an completely independent unit testing suite has been established within `test_project.py`. Powered by the `pytest` engine, these scripts utilize modern sandbox lifecycle triggers including custom `setup_module` and `teardown_module` algorithms. This allows the system to verify individual software behaviors in complete isolation, dynamically creating and instantly wiping out pristine operational databases for every validation sequence without disrupting the user's production logging data records.

## Summary of Execution and Conclusion
Ultimately, this project stands as a complete proof of modular design philosophy and robust data management guidelines. By decoupling presentation logic from underlying data mutations, the software guarantees maintainability and clear structural scalability for any future functional updates.
