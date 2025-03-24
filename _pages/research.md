---
layout: archive
title: "Research topics"
author_profile: true
redirect_from: 
  - /research/
  - /research.html
---

<br />

My research are mainly focused on numerical methods to solve **hyperbolic PDEs**. In particular,
I perform **stability analysis** (Fourier Analysis) of **high order methods**, as well as benchmarkings. 
So far, I studied particularly **explicite methods** in the **Eulerian formulation**, neverthless I am currently intering into **implicite/explicite** methods, 
in the **Lagrangian formulation** with adaptative remeshing technics. 

I also study, in a material deformation frame, **contact detection algorithms** to evaluate the most accuratly the dynamical response of materials.

<!-- ------------------------------------------------------------------------------------------------------------------------------------ -->


<hr style="border:1px solid #345a8c">
<!-- #345a8c -->

Continuous Galerkin high order methods to solve hyperbolic equations
---------------------------------------------------------------------
<!-- ### Numerical models -->
During my PhD, I interested in the construction of high order stabilised Continuous Galerkin formulation to solve hyperbolic equations. In particular, I studied
* different polynomial approximations as well as spatial discretisations and their construction (1D and 2D) in a finite elements frame;
* different time integrations methods;
* different stabilisation technics.
<!-- 1. Lagrange polynomials, which are the classical used for FE formulations, with -->
  <!-- * Uniforme discretisation, the classical approach; -->
  <!-- * Fekete discretisation built to optimise interpolation formulas; -->
  <!-- * Gauss-Lobatto and Cubature discretisation built to optimise integration formulas; -->
<!-- 2. Bernstein polynomials, which verify additional properties besides the one for Lagrangian points (such as their integrals are positive).  -->

For more detail about numerical models, methodology and results, you can refer to my PhD manuscript available on [HAL](https://theses.hal.science/tel-03656234).

### Stability analysis
My research around stability analysis of numerical schemes aims to propose, through Fourier analysis, stability criterium and metric of interest in order to optimise numerical 
formulations of methods. In particular, I perform **mono and bi-dimensional fully discrete Von Neumann analysis** of **Finite Elements formalutions**. \\
Starting from linear advection problems and using the periodicity of the solution, 
<!-- $$
\begin{align*}
     \left  \{
    \begin{array}{lll}
   \partial_t u + a   \partial_x u = 0, \qquad & \quad x\in[0,1] \\
	u(x,t) &= Ae^{i(kx - \xi t)} & \quad \mbox{with} \quad \xi = \omega + i \epsilon \\
	 & = Ae^{i(kx-\omega t)}e^{\epsilon t} & \quad i=\sqrt{-1}\\
	\end{array}	
    \right . 
\end{align*}
$$ -->
<!-- $$\omega$$ the phase, $$\epsilon$$ the damping rate and $$k=2\pi/\lambda$$ the wavenumber ($$\lambda$$ the wavelength). \\
Using the **periodicity** of the solution% and denoting by $$K\pm1$$ the neighboring elements, we have the discrete solution 
$$
\begin{equation*}
\widetilde{\mathbf{U}}_{K_{i\pm 1}} = e^{\pm i\theta}\widetilde{\mathbf{U}}_{K_i}, \theta:=  k\Delta x
\label{eq_ad_fourier0}
\end{equation*}
$$
![fig1](images/about/Fourier_1D_periodicity.png){: width="80%"} \\ -->
the **spatial and temporale discretisation** of numerical schemes allows to write: $$\forall$$ explicite numerical schemes: 
<p style="text-align: center;"> $$ \widetilde{\mathbf{U}}^{n+1} = G(\theta ,{\color{red} CFL},{\color{red} \delta}) \widetilde{\mathbf{U}}^{n} $$ </p> 
with $$G$$ the amplification matrix. Then, we can define <u>stability criterium</u> and <u>metric of interest</u> in the amplification matrix in order to optimise 
$${\color{red} CFL},{\color{red} \delta}$$ for any $$\theta$$, for all numerical schemes:
![fig1](images/about/Fourier_full_disc.png){: width="70%"} 

**NB:** Independantly, we can also perform partial discrete stability analysis: 
* Spatial analysis - dispersion curves : \\
  ![fig1](images/about/Fourier_space.png){: width="80%"} 
* Temporal analysis - dispersion curves of differents SSPRK schemes: \\
  ![fig1](images/about/Fourier_SSPRK.png){: width="60%"} 
  
### Coastal hydrodynamic issues

In the coastal hydrodynamic frame, several **challenges** appear and has to be take into account. In particular, I study several type of formulations:
* Wave propagation with a **high accuracy**: through *high order methods*;
* **Preservation of the lake at rest**: through *Well-balanced* formulation; \\
  Example of *Basic* $$\mathbb{P}_1$$ element, SSPRK & OSS: \\
  ![fig1](images/about/LakeAtRest_P1Basic.png){: width="80%"} \\
  Adding a perturbation on the left boundary \\
  ![fig2](images/about/LakeAtRest_Cub_perturbation.png){: width="80%"}
* **Shock/discontinuities capturing technique**: through additional *artificial viscosity* terms; \\
  Example of an asymetric break of a dam:\\
  ![fig3](images/about/DamBreakIC.png){: width="60%"} \\
  ![fig3](images/about/DamBreakEntropy.png){: width="80%"} 


<!-- ### Benchmarking -->

For more detail about methodology and results, you can refer to my PhD manuscript available on [HAL](https://theses.hal.science/tel-03656234).

**Main collaborators for this topic:** [Mario Ricchiuto](https://team.inria.fr/cardamom/marioricchiuto/) and [Davide Torlo](https://davidetorlo.it/).


**For students who are interested in these topics**, the CARDAMOM team propose some master thesis, PhD and post-doctoral positions! Have a look on the associated [page](https://team.inria.fr/cardamom/job-offers/).

<!-- <hr style="border:1px solid #345a8c"> -->
<!-- #345a8c -->

<!-- Continuous Galerkin high order methods to solve hyperbolic equations -->
<!-- --------------------------------------------------------------------- -->

<!-- ------------------------------------------------------------------------------------------------------------------------------------ -->

<hr style="border:1px solid #345a8c">

Numerical methods for multibodies deformation problems
-------------------------------------------

During my postdoctoral fellow at the CEA, I focused on developing innovative numerical methods for simulating the dynamic behavior of materials under intense stress.

### Numerical models

To evaluate the dynamical behaviour of materials, we can base on Euler's equations, which can describe the elasto-plastic physics of materials, in a Lagrangian formulation, with cell-centered and collocated **Finite Volume schemes**.\\
![fig8](images/about/FV_cells.png){: width="80%"} \\
In particular, I use **SGH** (*Staggered-Grid Hydrodynamics*) and **CLH** (*Collocated Lagrangian Hydrodynamics*) schemes in 1D, 2D, and 3D (see R. Loubere or P.H. Le Maire et al. works) for solving the Euler equations.

### Contact detection algorithm
Concerning the **contact detection procedure**, based on a Lagrangian approach to the numerical problem, several algorithms exist in the literature, mainly based on collision/penetration detection via a node-to-segment (NTS) technique (see article L. De Lorenzis et al. works and the references therein).
However, these methods do not provide information on the exact time of contact or its location. Moreover, for particularly complex geometries, the cost of the detection algorithm increases and can lead to unphysical situations.

To overcome these problems, I proposed a new algorithm, based on **Thales's theorem**, and usable for $$n$$-dimensional problems, $$n\in\mathbb{N}$$.
This technique, which I called **CETT** (*Continuous Extension of the Thales Theorem*), allows for precise (or even exact) detection of contact time and location.

The definition of this technique is quite intuitive in 2D since it is based on a collinearity condition between two vectors, which can also be expressed as solving a quadratic equation. The interpretation of the **CETT** for one-dimensional problems is straightforward. Finally, the extension to three-dimensional space is more complex in that the collinearity condition is satisfied from a vector product with two unknowns, and the three resulting terms of the vector product are not necessarily zero, unlike two-dimensional problems where the vector product yields a single component in $$\vec{z}$$.

This project is very innovative in the sense that until now, no multidimensional contact detection technique has been proposed in the literature, providing the time and position of contact, with an accuracy of order $$> 1$$.

![gifcontact3D](/images/gif/contact/output_3D_diagonal_sphere.gif){: width="40%"}
![gifcontact3D](/images/gif/contact/output_2D_diagonal_circle.gif){: width="40%"}

For more detail about the multidimensional algorithm, you can refer to my recent paper about this subject available on [HAL](https://cea.hal.science/DAM/hal-04981784v1).

**Main collaborators for this topic:** [Gael Poette](https://site-imb.math.u-bordeaux.fr/fr/fiche-personnelle-gpoette) and Nicolas Therme (CEA CESTA).


**For students who are interested in these topics**, the CEA propose some master thesis, PhD and Post-doctoral positions. You can visit related pages [here](https://www.emploi.cea.fr/offre-de-emploi/liste-toutes-offres.aspx?changefacet=1&facet_Contract=1781) or [here](https://www-dam.cea.fr/damidf/offres-theses-et-post-doc/
).




<!-- ------------------------------------------------------------------------------------------------------------------------------------ -->

<hr style="border:1px solid #345a8c">

Weather routing studies
-------------------------------------------

To meet decarbonization objectives in maritime transport, weather routing plays an important role. In this context, [D-ICE Engineering](https://www.dice-engineering.com/) has developed a versatile, efficient, and robust multi-objective weather routing algorithm to reduce vessel fuel consumption.
Among other things, [D-ICE Engineering](https://www.dice-engineering.com/) acts as a third party for shipowners to calculate the potential benefits of routing through statistical weather routing studies (i.e., simulating hundreds of voyages over the past years, using historical weather data). 
However, since these statistics are based on specific inputs, biais can be introduced directly from study case inputs.

My main research at [D-ICE Engineering](https://www.dice-engineering.com/) was part this frame, to quantify the biais introduced by different factors in statistical weather routing study, and also the optimisation of operational weather routing algorithm.. 

<!-- ### Use the wind to save the world (and your wallet) -->

### Some research studies 
* **Crystal effect**: Statistical studies being based on historical weather data, a biais is straightly introduce beacause in an operational context, only weather forecasts are available. 
 I therefore proposed a study to highlight the bias introduced by the input meteorological data, as well as various factors that could impact it. I also proposed a study on the impact of routing update frequency (and weather forecasts) on operational routing.
* **Bias introduced by statistical samples** (in terms of travel departure dates): To this end, I defined convergence metrics as well as precision criteria to quantify deviations from "optimal" data.
* **Operational routing algorithm optimization**: if we consider a weather model providing forecasts for X days, it is possible to have routes that exceed this forecast duration. I then proposed different algorithms to define the optimal route in an operational framework,
based on metrics defining risk exposures according to the options (*Pareto optimal*);
* **Horizon trust study**: Continuing this work, using 10-day forecast models, I defined the trust horizon variable. I then evaluated the impact of this variable on routing quality.

And other smaller projects
* Impact of ship performance modeling in routing;
* Impact of wave consideration in routing performance;
* Impact of degradation of routing algorithms on performance.

<!-- Section in building ![gifship](images/gif/ship_gif.gif){: width="40%"} -->

**Main collaborators for this topic:** Maxime Dupuy (D-ICE Engineering) and Frédéric Deybach (Total Energies).

**For students who are interested in these topics**, D-ICE is looking for its futur talents! Have a look on the associated [career page](https://www.dice-engineering.com/carriere).


<!-- Getting started
======
1. Register a GitHub account if you don't have one and confirm your e-mail (required!)
1. Fork [this template](https://github.com/academicpages/academicpages.github.io) by clicking the "Use this template" button in the top right. 
1. Go to the repository's settings (rightmost item in the tabs that start with "Code", should be below "Unwatch"). Rename the repository "[your GitHub username].github.io", which will also be your website's URL.
1. Set site-wide configuration and create content & metadata (see below -- also see [this set of diffs](http://archive.is/3TPas) showing what files were changed to set up [an example site](https://getorg-testacct.github.io) for a user with the username "getorg-testacct")
1. Upload any files (like PDFs, .zip files, etc.) to the files/ directory. They will appear at https://[your GitHub username].github.io/files/example.pdf.  
1. Check status by going to the repository settings, in the "GitHub pages" section

Site-wide configuration
------
The main configuration file for the site is in the base directory in [_config.yml](https://github.com/academicpages/academicpages.github.io/blob/master/_config.yml), which defines the content in the sidebars and other site-wide features. You will need to replace the default variables with ones about yourself and your site's github repository. The configuration file for the top menu is in [_data/navigation.yml](https://github.com/academicpages/academicpages.github.io/blob/master/_data/navigation.yml). For example, if you don't have a portfolio or blog posts, you can remove those items from that navigation.yml file to remove them from the header. 

Create content & metadata
------
For site content, there is one markdown file for each type of content, which are stored in directories like _publications, _talks, _posts, _teaching, or _pages. For example, each talk is a markdown file in the [_talks directory](https://github.com/academicpages/academicpages.github.io/tree/master/_talks). At the top of each markdown file is structured data in YAML about the talk, which the theme will parse to do lots of cool stuff. The same structured data about a talk is used to generate the list of talks on the [Talks page](https://academicpages.github.io/talks), each [individual page](https://academicpages.github.io/talks/2012-03-01-talk-1) for specific talks, the talks section for the [CV page](https://academicpages.github.io/cv), and the [map of places you've given a talk](https://academicpages.github.io/talkmap.html) (if you run this [python file](https://github.com/academicpages/academicpages.github.io/blob/master/talkmap.py) or [Jupyter notebook](https://github.com/academicpages/academicpages.github.io/blob/master/talkmap.ipynb), which creates the HTML for the map based on the contents of the _talks directory).

**Markdown generator**

The repository includes [a set of Jupyter notebooks](https://github.com/academicpages/academicpages.github.io/tree/master/markdown_generator
) that converts a CSV containing structured data about talks or presentations into individual markdown files that will be properly formatted for the Academic Pages template. The sample CSVs in that directory are the ones I used to create my own personal website at stuartgeiger.com. My usual workflow is that I keep a spreadsheet of my publications and talks, then run the code in these notebooks to generate the markdown files, then commit and push them to the GitHub repository.

How to edit your site's GitHub repository
------
Many people use a git client to create files on their local computer and then push them to GitHub's servers. If you are not familiar with git, you can directly edit these configuration and markdown files directly in the github.com interface. Navigate to a file (like [this one](https://github.com/academicpages/academicpages.github.io/blob/master/_talks/2012-03-01-talk-1.md) and click the pencil icon in the top right of the content preview (to the right of the "Raw | Blame | History" buttons). You can delete a file by clicking the trashcan icon to the right of the pencil icon. You can also create new files or upload files by navigating to a directory and clicking the "Create new file" or "Upload files" buttons. 

Example: editing a markdown file for a talk
![Editing a markdown file for a talk](/images/editing-talk.png)

For more info
------
More info about configuring Academic Pages can be found in [the guide](https://academicpages.github.io/markdown/), the [growing wiki](https://github.com/academicpages/academicpages.github.io/wiki), and you can always [ask a question on GitHub](https://github.com/academicpages/academicpages.github.io/discussions). The [guides for the Minimal Mistakes theme](https://mmistakes.github.io/minimal-mistakes/docs/configuration/) (which this theme was forked from) might also be helpful. -->
