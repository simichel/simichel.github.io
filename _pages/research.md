---
layout: archive
title: "Research topics"
permalink: /research/
author_profile: true
redirect_from:
  - /research
---

<br />

My research focuses mainly on numerical methods for **hyperbolic PDEs**, with a particular interest in **stability analysis** of **high-order methods** and benchmark design. So far, I have mostly worked on **explicit schemes** in an **Eulerian formulation**; I am now also interested in **implicit-explicit strategies** in **ALE and Lagrangian formulations**, including adaptive remeshing techniques.

I also work on **contact detection algorithms** for material deformation problems, with the goal of accurately capturing contact time and location in dynamic simulations.

<!-- ------------------------------------------------------------------------------------------------------------------------------------ -->


<hr style="border:1px solid #345a8c">
<!-- #345a8c -->

High-order Continuous Galerkin methods for solving hyperbolic equations
---------------------------------------------------------------------
<!-- ### Numerical models -->
During my PhD, I worked on the construction of high-order stabilised Continuous Galerkin formulations for hyperbolic equations. In particular, I studied
* polynomial approximations and their associated spatial discretisations in one and two spatial dimensions;
* explicit time integration methods;
* stabilisation strategies for continuous finite element schemes.
<!-- 1. Lagrange polynomials, which are the classical used for FE formulations, with -->
  <!-- * Uniforme discretization, the classical approach; -->
  <!-- * Fekete discretization built to optimise interpolation formulas; -->
  <!-- * Gauss-Lobatto and Cubature discretization built to optimise integration formulas; -->
<!-- 2. Bernstein polynomials, which verify additional properties besides the one for Lagrangian points (such as their integrals are positive).  -->

More details on the numerical models, methodology, and results are available in my PhD manuscript on [HAL](https://theses.hal.science/tel-03656234).

### Stability analysis
My work on stability analysis uses Fourier techniques to define stability criteria and diagnostic quantities for comparing numerical formulations. In particular, I perform **one- and two-dimensional fully discrete Von Neumann analyses** of **finite element formulations**.

Starting from linear advection problems and using periodicity, the **spatial and temporal discretisations** of an explicit scheme lead to an amplification matrix:
<p style="text-align: center;"> $$ \widetilde{\mathbf{U}}^{n+1} = G(\theta ,{\color{red} CFL},{\color{red} \delta}) \widetilde{\mathbf{U}}^{n} $$ </p> 
The matrix $$G$$ is then used to define stability criteria and diagnostic quantities, and to optimise $${\color{red} CFL}$$ and stabilisation parameters such as $${\color{red} \delta}$$ for all wavenumbers $$\theta$$.
<p style="text-align: center;"><img src="/images/research/about/Fourier_full_disc.png" alt="Fully discrete Fourier stability analysis" style="width: 62%;"></p> 

**NB:** Partially discrete analyses are also useful:
* Spatial analysis - dispersion curves:
  <p style="text-align: center;"><img src="/images/research/about/Fourier_space.png" alt="Spatial dispersion curves" style="width: 70%;"></p> 
* Temporal analysis - dispersion curves for different SSPRK schemes:
  <p style="text-align: center;"><img src="/images/research/about/Fourier_SSPRK.png" alt="Temporal dispersion curves for SSPRK schemes" style="width: 52%;"></p> 
  
### Coastal hydrodynamics

Coastal hydrodynamics raises several numerical challenges. In this context, I have worked on formulations addressing:
* accurate wave propagation, using *<u>high-order methods</u>*;
* **lake-at-rest preservation**, using *<u>well-balanced</u>* formulations.
  Example with a basic $$\mathbb{P}_1$$ element, SSPRK time integration, and OSS stabilisation:
  <p style="text-align: center;"><img src="/images/research/about/LakeAtRest_P1Basic.png" alt="Lake at rest benchmark with P1 element" style="width: 70%;"></p>
  Adding a perturbation on the left boundary:
  <p style="text-align: center;"><img src="/images/research/about/LakeAtRest_Cub_perturbation.png" alt="Lake at rest perturbation benchmark" style="width: 70%;"></p>
* **shock and discontinuity capturing**, using additional *<u>artificial viscosity</u>* terms and **MOOD cascade** strategies.
  Example of an asymmetric dam-break configuration:
  <p style="text-align: center;"><img src="/images/research/about/DamBreakIC.png" alt="Asymmetric dam break initial condition" style="width: 52%;"></p>
  <p style="text-align: center;"><img src="/images/research/about/DamBreakEntropy.png" alt="Asymmetric dam break entropy viscosity result" style="width: 70%;"></p> 


<!-- ### Benchmarking -->

More details on the methodology and results are available in my PhD manuscript on [HAL](https://theses.hal.science/tel-03656234).

**Main collaborators for these topics:** [Mario Ricchiuto](https://team.inria.fr/cardamom/marioricchiuto/) and [Davide Torlo](https://davidetorlo.it/).


**For students interested in these topics**, the CARDAMOM team regularly offers master's thesis projects, PhD positions, and postdoctoral positions. Have a look at the associated [page](https://team.inria.fr/cardamom/job-offers/).

<!-- <hr style="border:1px solid #345a8c"> -->
<!-- #345a8c -->

<!-- Continuous Galerkin high-order methods to solve hyperbolic equations -->
<!-- --------------------------------------------------------------------- -->

<!-- ------------------------------------------------------------------------------------------------------------------------------------ -->

<hr style="border:1px solid #345a8c">

Stability analysis for shifted-boundary CG discretisations
-------------------------------------------

*Section in preparation.*

**Main collaborator for this topic:** [Mirco Ciallella](https://sites.google.com/view/mircociallella/research).


<!-- ------------------------------------------------------------------------------------------------------------------------------------ -->

<hr style="border:1px solid #345a8c">

High-order ADER-AFE-DG methods on polyhedral meshes
-------------------------------------------

Many CFD applications require numerical methods that can handle **complex geometries**, **unstructured meshes**, high-order accuracy, and robust stabilisation near discontinuities. A natural difficulty is that high-order methods are well established on classical elements such as triangles, quadrilaterals, tetrahedra, or hexahedra, while arbitrary polygonal and polyhedral meshes do not come with a universal reference element.

<p style="text-align: center;"><img src="/images/research/alps/cg_dg_formulation.png" alt="Classical CG and DG formulations on tetrahedral meshes" style="width: 62%;"></p>

In this context, I work on **ADER-AFE-DG schemes** for nonlinear hyperbolic systems, especially compressible Euler and Navier-Stokes equations. The main idea is to combine a discontinuous Galerkin formulation at the polyhedral-cell level with an **Agglomerated Finite Element (AFE)** representation built on an internal tetrahedral subgrid. This keeps the implementation close to standard finite element technology while preserving the flexibility of polyhedral meshes.

The current methodology combines:
* **continuous AFE basis functions** inside each arbitrary polyhedral element;

  <p style="text-align: center;"><img src="/images/research/alps/afe_construction.png" alt="Agglomerated finite element construction inside a polyhedral cell" style="width: 62%;"></p>
* a **DG formulation** across polyhedral interfaces;

  <p style="text-align: center;"><img src="/images/research/alps/afe_dg_composite.png" alt="Agglomerated finite element discontinuous Galerkin formulation" style="width: 62%;"></p>
* **one-step ADER time integration** based on a local space-time predictor;

  <p style="text-align: center;"><img src="/images/research/alps/ader_time_integration.png" alt="One-step ADER time integration based on a local space-time predictor" style="width: 62%;"></p>
* local artificial viscosity for shock capturing and stabilisation.

  Example of a **3D spherical explosion** benchmark:
  <p style="text-align: center;"><img src="/images/research/alps/spherical_explosion_viscosity.png" alt="Artificial viscosity for shock capturing on a 3D spherical explosion benchmark" style="width: 72%;"></p>

Ongoing developments also concern the extension of this framework to **ALE formulations**, in which the mesh can move with an arbitrary velocity, and to **IMEX strategies**, where stiff source terms, relaxation, or diffusive contributions can be treated implicitly while preserving the explicit ADER-DG structure when possible.

**Main collaborators for these topics:** [Walter Boscheri](https://www.lama.univ-savoie.fr/members/default/boscheriw) and Lorenzo Diazzi.


<!-- ------------------------------------------------------------------------------------------------------------------------------------ -->

<hr style="border:1px solid #345a8c">

Numerical methods for multi-body deformation problems
-------------------------------------------

During my postdoctoral fellowship at CEA, I worked on numerical methods for simulating the dynamic behaviour of materials under intense stress.

### Numerical models

To model the dynamic behaviour of materials, I worked with Lagrangian formulations of the Euler equations and cell-centred or collocated **finite-volume schemes**.
<p style="text-align: center;"><img src="/images/research/about/FV_cells.png" alt="Finite volume cells" style="width: 70%;"></p>
In particular, I use **SGH** (*Staggered-Grid Hydrodynamics*) and **CLH** (*Collocated Lagrangian Hydrodynamics*) schemes in 1D, 2D, and 3D (see, for example, the work of R. Loubère and P.-H. Maire et al.) to solve the Euler equations.

### Contact detection algorithm
For the **contact detection procedure** in Lagrangian simulations, several algorithms exist in the literature. Many of them rely on collision or penetration detection through node-to-segment (NTS) techniques; see, for instance, the work of L. De Lorenzis et al. and the references therein.
However, these methods do not provide information on the exact time of contact or its location. Moreover, for particularly complex geometries, the cost of the detection algorithm increases and can lead to nonphysical situations.

To overcome these limitations, I proposed a new algorithm based on **Thales' theorem**, usable for $$n$$-dimensional problems, $$n\in\mathbb{N}$$.
This technique, called **CETT** (*Continuous Extension of Thales' Theorem*), enables precise—and, in some cases, exact—detection of contact time and location.

In 2D, the construction is quite intuitive: it relies on a collinearity condition between two vectors, which can also be written as a quadratic equation. The one-dimensional interpretation of **CETT** is straightforward. The three-dimensional extension is more involved, because the collinearity condition is expressed through a vector product with two unknowns, and the three resulting components are not necessarily zero simultaneously.

To the best of my knowledge, this is the first multidimensional contact detection technique that provides both contact time and contact position with an order of accuracy greater than one.

<p style="text-align: center;">
  <img src="/images/research/gif/contact/output_3D_diagonal_sphere.gif" alt="3D diagonal sphere contact detection" style="width: 38%;">
  <img src="/images/research/gif/contact/output_2D_diagonal_circle.gif" alt="2D diagonal circle contact detection" style="width: 38%;">
</p>

More details on the multidimensional algorithms are available in my recent paper on [HAL](https://cea.hal.science/DAM/hal-04981784v1).

**Main collaborators for these topics:** [Gaël Poëtte](https://site-imb.math.u-bordeaux.fr/fr/fiche-personnelle-gpoette) and Nicolas Therme (CEA CESTA).


**For students interested in these topics**, CEA offers master's thesis projects, PhD positions, and postdoctoral positions. You can visit related pages [here](https://www.emploi.cea.fr/offre-de-emploi/liste-toutes-offres.aspx?changefacet=1&facet_Contract=1781) or [here](https://www-dam.cea.fr/damidf/offres-theses-et-post-doc/
).


<!-- ------------------------------------------------------------------------------------------------------------------------------------ -->

<hr style="border:1px solid #345a8c">

Weather routing studies
-------------------------------------------

Weather routing plays an important role in reducing fuel consumption and supporting decarbonization objectives in maritime transport. In this context, [D-ICE Engineering](https://www.dice-engineering.com/) has developed a versatile and robust multi-objective *<u>weather routing algorithm</u>*.
[D-ICE Engineering](https://www.dice-engineering.com/) also performs statistical *weather routing studies* for shipowners, by simulating hundreds of voyages over past years using historical weather data. 
However, these statistics depend strongly on the study inputs, which can introduce biases directly into the analysis.

<p style="text-align: center;"><img src="/images/research/about/crystal_graph.png" alt="Transatlantic graph illustration" style="width: 55%;"></p>

My work at [D-ICE Engineering](https://www.dice-engineering.com/) focused on **quantifying biases in statistical *weather routing studies*** and **optimising operational *weather routing algorithms***.

<!-- ### Use the wind to save the world (and your wallet) -->

### Selected research studies
* **Crystal effect**: Because statistical studies are based on historical weather data, they introduce a bias with respect to operational conditions, where only weather forecasts are available. 
  I therefore proposed a study to highlight the bias introduced by the input meteorological data, as well as various factors that could influence it. I also proposed a study on the impact of routing update frequency (and weather forecasts) on operational routing.

  <p style="text-align: center;"><img src="/images/research/about/crystal_operational.png" alt="Historical and operational weather routing comparison" style="width: 70%;"></p>
* **Bias introduced by statistical samples**: I defined convergence metrics and precision criteria to quantify the effect of departure-date sampling.
* **Operational routing algorithm optimisation**: when a route exceeds the forecast horizon of a weather model, the optimisation must account for uncertainty beyond the available forecast. I proposed routing strategies based on risk-exposure metrics and Pareto-optimal choices;
* **Horizon trust study**: Continuing this work, using 10-day forecast models, I defined the trust horizon variable. I then evaluated the impact of this variable on routing quality.

Other smaller projects include:
* impact of ship performance modelling in routing;
* impact of wave modelling on routing performance;
* impact of degraded routing algorithms on performance.

<!-- Section in building ![gifship](images/gif/ship_gif.gif){: width="40%"} -->

**Main collaborators for these topics:** Maxime Dupuy (D-ICE Engineering) and Frédéric Deybach (TotalEnergies).

**For students interested in these topics**, D-ICE is looking for future talents. Have a look at the associated [career page](https://www.dice-engineering.com/carriere).
