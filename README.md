[![LinkedIn][linkedin-shield]][linkedin-url]
[![Blog][hashnode-shield]][hashnode-url]

<br />
<div>

<h3 align="center">Student-Courses backend for unit testing</h3>

  <p align="center">
    Student with mobiles and courses project with unit tests and coverage
</div>

<!-- ABOUT THE PROJECT -->
## About The Project
Using Django framework, I have built a project where we have a table of students, also a table of 
mobiles associated with students (Many to One). Also a table of courses with a many-to-many relationship with the
 students. Also added unit tests and coverage as a follow up for this [article](https://zomor.hashnode.dev/django-unit-testing-part-12-testing-and-coverage-concepts)
<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [![Python][Python]][Python-url]
* [![Django][Django]][Django-url]
* [![sqlite][sqlite]][sqlite-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started


### Prerequisites

* Python <= 3.10.6
* Pip <= 22.0.2
* Python virtual environment

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/elZomor/unit_testing_project.git && cd unit_testing_project
   ```
2. Create virtual environment
   ```sh
   python3 -m venv venv
   ```
3. Activate virtual environment
   ```sh
   source venv/bin/activate
   ```
4. Install requirements
   ```sh
   pip install -r requirements.txt
   ```
5. Migrate models
   ```sh
   python manage.py migrate
   ```
6. Run server
   ```sh
   python manage.py runserver 0.0.0.0:8002
   ```
<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Please follow the link in the blog here


[Part1: Concepts](https://zomor.hashnode.dev/django-unit-testing-part-12-testing-and-coverage-concepts)


[Part2: Implementation](https://zomor.hashnode.dev/django-unit-testing-part-22-testing-and-coverage-implementation)
<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CONTACT -->
## Contact

Mohamed Elzomor - mohamed.ali.elzomor@gmail.com

Project Link: [https://github.com/elZomor/unit_testing_project](https://github.com/elZomor/unit_testing_project)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/mohamed-elzomor
[hashnode-shield]: https://img.shields.io/badge/-Blog-black.svg?style=for-the-badge&colorB=555
[hashnode-url]: https://zomor.hashnode.dev/
[Django]: https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green
[Django-url]: https://docs.djangoproject.com/en/3.2/
[GraphQL]: https://img.shields.io/badge/GraphQl-E10098?style=for-the-badge&logo=graphql&logoColor=white
[GraphQL-url]: https://graphql.org/
[Python]: https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue
[Python-url]: https://docs.python.org/3/
[sqlite]: https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white
[sqlite-url]: https://www.sqlite.org/index.html
[JWT]: https://img.shields.io/badge/JWT-000000?style=for-the-badge&logo=JSON%20web%20tokens&logoColor=white
[JWT-url]: https://jwt.io/
