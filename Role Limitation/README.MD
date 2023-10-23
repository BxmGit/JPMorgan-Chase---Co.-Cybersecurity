# Design and Develop a System to Tighten Access to Sensitive Information

## Summary
In this project, my goal was to design a system that simulates the limitation of active roles a user can hold at any given point in time. This task is crucial for enforcing least privilege in access control systems, ensuring that users have only the minimal set of roles required, thereby reducing risk in case of account compromises.

## Background
Users with an extensive set of roles pose a significant risk to organizations, especially if their accounts get compromised. The system I designed aims to automate the enforcement of least privilege, minimizing the number of active roles a user has and removing any unnecessary roles.

## Task Overview
For the fourth module of this project, my objectives were:

1. Set up my development environment, ensuring all necessary tools, dependencies, and files were properly installed and configured.
2. Complete a coding exercise that simulates a system managing user roles, adhering to the least privilege principle.
3. Optionally, review additional resources to deepen my understanding of the topic.

The main deliverable was the `RolesCache` class, implemented in `task4.py`, which I uploaded upon completion.

### Development Process
The process involved implementing the `RolesCache` class with methods to get and set user roles, ensuring that the number of active roles did not exceed a specified capacity. The class also keeps track of the last used roles to efficiently remove the oldest role when necessary.

### Purpose
The primary goal was to understand and implement a system that enforces least privilege in access control, a crucial aspect of securing sensitive information and systems.

### Conclusion
This project provided me with valuable experience in designing and implementing access control systems, specifically in managing user roles and enforcing least privilege. The skills and knowledge gained are applicable in various security and software development contexts, enhancing my ability to contribute to secure system design and implementation.
