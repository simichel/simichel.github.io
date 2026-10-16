---
layout: archive
title: "Curriculum Vitae"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}
<!-- /home/smichel/documents/sixtinemichel.github.io/files/publications/Finite_Element_Methods_for_Shallow_Water_Equations.pdf -->
<div style="text-align: right"> <a href="/files/publications/Finite_Element_Methods_for_Shallow_Water_Equations.pdf"><b>PDF version </b></a> </div>

<i class="fa-solid fa-graduation-cap"></i> Education
------------------------------------------------
* **PhD in Applied Mathematics** - [University of Bordeaux](https://www.u-bordeaux.fr/), Talence, 2022 - [HAL](https://theses.hal.science/tel-03656234) or [theses.fr](https://theses.fr/2022BORD0050).
* **Master's degree in Computational Science and Modelling** - [University of Rennes 1](https://www.univ-rennes.fr/), Rennes, 2018
* **Bachelor's degree in Mathematics, Computing and Statistics** - [University of South Brittany](https://www.univ-ubs.fr/fr/index.html), Vannes, 2016

<i class="fa-solid fa-square-root-variable"></i> Work experience
------------------------------------------------------
* **Since Sept. 2025: Assistant Professor (*enseignant-chercheur*)** - [ESILV](https://www.esilv.fr/) / [DVRC - De Vinci Research Center](https://www.devinci.fr/research-center/), Paris (France)
  * Teaching activities at ESILV.
  * Research activities at DVRC on high-order methods for hyperbolic PDEs and related stability analyses.

* **Dec. 2024 to Aug. 2025: Postdoctoral position** - University of Ferrara, Ferrara (Italy)
  * Structure-preserving schemes for hyperbolic systems of conservation laws and kinetic equations.
  <!-- * Development and implementation of novel 3D and high order structure preserving scheme: -->
  <!-- Continuous Finite Element subgrid basis functions for Discontinuous Galerkin schemes on unstructured polygonal Voronoi meshes. -->
  * Supervisor: Walter Boscheri

* **Jan. 2023 to Dec. 2024: Project manager and R&D engineer** - D-ICE Engineering, Nantes (France)
  * Statistical historical weather routing study (with R&D topics).
  * Software development and maintenance.
  * Preparation of commercial proposals, workload planning, and project management.

* **March 2022 to Jan. 2023: Postdoctoral position** - CEA, Le Barp (France)
  * Development of new numerical methods for contact simulations.
  <!-- * Development of a Finite Volumes (FV) library in the lagrangian formulation to solve hyperbolic equations. -->
  <!-- * Development and analysis of multidimensional contact detection methods. -->
  * Supervisor: Nicolas Therme
  
* **Nov. 2018 to March 2022: PhD student** - INRIA, Talence (France)
  * Finite Element Methods for Shallow Water Equations: Analysis, Modeling and Applications to Coastal Hydrodynamics.
  <!-- * Development from scratch of a Python stabilized Continuous Galerkin (CG) Finite Elements (FE) library, to solve hyperbolic equations. -->
  <!-- * One and two dimensional Von Neumann analysis. -->
  <!-- * Implementation of a CG/DG-FEM in a C++ code (aerosol). -->
  * Supervisor: Mario Ricchiuto
  
* **Oct. 2017 to Oct. 2018: Research intern (Master's thesis)** - CEA, Bruyères-le-Châtel (France)
  * Optimisation and implementation of a tsunami-modelling code.
  <!-- * Implementation of a 2D Finite Difference (FD) and Volume (FV) schemes. -->
  * Supervisor: Philippe Heinrich
  
* **May to Jul. 2017: Research intern** - University of Bristol, Bristol (United Kingdom)
  * Modelling and analysis of deformation and buckling in homogeneous materials.
  * Supervisor: Anton Shterenlikht

  
<i class="fa-solid fa-laptop"></i> Skills
------------------
* **Scientific programming:** Fortran, C/C++, Python, MATLAB
* **Software:** Gmsh, ParaView, Power BI, Abaqus, COMSOL Multiphysics
  <!-- * Sub-skill 2.1-->
  <!-- * Sub-skill 2.2 -->
  <!-- * Sub-skill 2.3  -->
* **Tools and libraries:** Git and CI, LaTeX, pybind11, Sphinx documentation, AWS

<i class="fa-solid fa-file"></i> Publications
------------------
  <ul>{% for post in site.publications reversed %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>
  
<i class="fa-solid fa-users"></i> Talks
------------------
  <ul>{% for post in site.talks reversed %}
    {% include archive-single-talk-cv.html  %}
  {% endfor %}</ul>
  
<i class="fa-solid fa-chalkboard-user"></i> Teaching
------------------
Selected teaching activities in mathematics.

<ul class="cv-teaching-list">
{% assign teaching_posts = site.teaching | sort: "teaching_order" %}
{% for post in teaching_posts %}
  <li>{{ post.title }} - {{ post.type }}, {{ post.venue }}, ({{ post.academic_year }} - {{ post.semester }})</li>
{% endfor %}
</ul>

<style>
.cv-teaching-list {
  margin-top: 0.4rem;
  padding-left: 1.2rem;
}
.cv-teaching-list li {
  margin-bottom: 0.25rem;
  font-size: 0.95rem;
  line-height: 1.35;
}
</style>
  
<!-- Service and leadership
======
* Currently signed in to 43 different slack teams -->



<i class="fa-solid fa-tags"></i> Various certifications
------------------------------------------------------
* <i class="fa-solid fa-fish"></i> **Scuba diving PA20/PE40:** French Level 2 scuba diving certification, held since 2019
* <i class="fa-sharp-duotone fa-solid fa-life-ring"></i> **BNSSA:** French water-safety and rescue qualification, held since 2016; refresher training completed in 2026
* <i class="fa-solid fa-briefcase-medical"></i> **PSE1:** Team First Aid Level 1 certification, held since 2016; refresher training completed in 2026
* <i class="fa-solid fa-sailboat"></i> **CQP AMV:** Sailing instructor certification, held since 2014
* <i class="fa-solid fa-car"></i> **Driving licence:** held since 2014
* <i class="fa-solid fa-puzzle-piece"></i> **BAFA:** Holiday-camp activity leader qualification, held since 2013
* <i class="fa-solid fa-ship"></i> **Coastal boating licence:** held since 2012
<!-- <i class="fa-solid fa-anchor"></i> -->
  <!-- * Sub-skill 2.1--> 
  <!-- * Sub-skill 2.2 -->
  <!-- * Sub-skill 2.3  -->

<i class="fa-solid fa-heart-pulse"></i> Other activities
------------------------------------------------------
* <i class="fa-solid fa-sailboat"></i> **Sailing:** Catamaran, windsurfing and kitesurfing; sailing instructor from 2013 to 2022.
* <i class="fa-solid fa-person-swimming"></i> **Swimming:** Returned to competitive swimming in 2024; coached swimming from 2010 to 2013 and in 2026; rankings available on the [FFN](https://ffn.extranat.fr/webffn/nat_recherche.php?idact=nat&idrch_id=989895&idbas=50) website.
* <i class="fa-solid fa-scissors"></i> **Sewing:** Personal sewing projects and handmade creations, available [here](/portfolio).

<!-- https://fontawesome.com/search?q=sail&o=r&ic=free&s=solid&ip=classic -->
