# Task Management System — Software Test Plan

## 1. Test Plan Identifier

**Document ID:** TMP-TP-001  
**Project:** Task Management System  
**Version:** 1.0  
**Testing Framework:** pytest  
**Application Framework:** Flask  
**Programming Language:** Python

## 2. Introduction

The Task Management System is a small web application that allows users to log in using predefined demo credentials and manage tasks. Users can add tasks, mark tasks as complete or incomplete, and delete tasks.

This test plan defines the testing scope, objectives, approach, environment, and criteria used to evaluate the application.

## 3. Test Items

The following components will be tested:

- Login functionality
- Password minimum-length validation
- Task display
- Adding tasks
- Completing tasks
- Marking tasks incomplete
- Deleting tasks
- Handling invalid login credentials
- Correctness of application responses

## 4. Features to Be Tested

1. Valid login using the configured demo credentials.
2. Invalid login using an incorrect password.
3. Rejection of passwords shorter than four characters.
4. Acceptance of the correct four-character demo password.
5. Display of predetermined tasks.
6. Addition of a non-empty task.
7. Completion and reversal of task completion.
8. Deletion of a selected task.

## 5. Features Not to Be Tested

The following are outside the scope of this project version:

- Database persistence
- User registration
- Password recovery
- Multi-user access
- Production security
- Performance under large numbers of concurrent users
- Deployment to a public server

## 6. Test Approach

### 6.1 Black-Box Testing

The application will be tested by providing inputs and checking observable outputs without relying on internal implementation details.

### 6.2 Boundary Value Analysis

Password validation will be tested around the four-character minimum:

- Three characters: reject.
- Four characters: allow length validation.
- Five characters: allow length validation, but authenticate only if the password is correct.

### 6.3 Automated Testing

pytest will execute automated tests. Python assertions will compare actual results with expected results.

### 6.4 Regression Testing

The complete test suite will be executed after code changes to check whether existing features still work.

## 7. Test Environment

- Operating System: Windows
- Python: 3.14.3
- Web Framework: Flask
- Test Framework: pytest 9.1.1
- Browser: Any supported modern browser for manual checks
- Execution Environment: Python virtual environment

## 8. Test Entry Criteria

Testing can begin when:

- The application starts without errors.
- Required dependencies are installed.
- The login page and dashboard are available.
- Test functions and fixtures are configured.

## 9. Test Exit Criteria

Testing is considered complete for this version when:

- All planned test cases have been executed.
- Failures have been investigated.
- Relevant defects have been fixed or documented.
- Final pytest results and quality metrics have been recorded.

## 10. Suspension and Resumption Criteria

Testing may be suspended if the application cannot start or a critical failure prevents further tests. Testing resumes after the blocking issue has been resolved.

## 11. Test Deliverables

- Test plan
- Test case specifications
- pytest source code
- Test execution results
- Code coverage report
- Defect reports
- Test metrics and quality measurements
- Final test summary report

## 12. Responsibilities

The student developer is responsible for implementation, test design, test execution, defect analysis, measurement, and preparation of the final report.

## 13. Risks and Assumptions

- The application uses predefined demo credentials.
- Tasks are stored in a Python list and reset when the application restarts.
- The current login does not implement session-based access protection.
- Test results depend on the correctness of the test environment and test assertions.

## 14. Approval

**Prepared by:** Student Developer  
**Reviewed by:** Faculty / Project Evaluator  
**Approval Date:** To be completed during submission