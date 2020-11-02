# webfront E2E tests
E2E Tests for bebas akun

## Branch Naming Convention
master: the branch for the production

develop: the branch for the staging

hotfix: hotfix/Issue number + "-" + sequential number ex) hotfix/199-1

new features: feature/Issue number + "-" + sequential number ex) feature/199-1


## General Developing Flow
1. A hotfix branch makes from master branch
2. A feature branch makes from master branch

## Installation under Ubuntu Linux platform
1. Makesure python3 & Python3 Pip are available in your OS
2. Clone the project
3. cd webfront_test
4. Create virtual environment: python3 -m venv venv
5. Activate virtual environment: source venv/bin/activate
6. Install dependencies: pip install -r requirements.txt
7. Your environment is ready