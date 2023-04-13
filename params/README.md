# What do these variables mean?

## Initial Values (initial_conditions.json)

```math
\begin{align*}
    r &: \text{The GDP of the richer, developed country. Must be non-negative}
    \\
    p &: \text{The GDP of the poorer developing country. Must be non-negative}
    \\
    c &: \text{The concentration of CO$_2$ in the atmosphere. Must be non-negative}
\end{align*}
```

## ODE System Parameter Values (ODE_params.json)

```math
\begin{align*}
    G_r &: \text{Growth rate of the richer country's GDP.}
    \\
    G_p &: \text{Growth rate of the poorer country's GDP.}
    \\
    K_r &: \text{Initial carrying capacity of the richer country's GDP. Must be strictly positive.}
    \\
    K_p &: \text{Initial carrying capacity of the poorer country's GDP. Must be strictly positive.}
    \\
    \gamma &: \text{Emission rate of CO$_2$ with respect to GDP. Must be non-negative.}
    \\
    \alpha &: \text{CO$_2$ emission efficiency from GDP due to innovation of the richer country. Must be non-negative.}
    \\
    \beta &: \text{CO$_2$ emission efficiency from GDP due to innovation of the poorer country. Must be non-negative.}
    \\
    D &: \text{Global disaster intensity. Must be non-negative.}
    \\
    f &: \text{Global disaster frequency. Must be a strictly positive integer.}
    \\
    I_n &: \text{Innovation growth rate. Must be non-negative}
    \\
    M_p &: \text{Modernization program: The amount of innovation that the richer country donates
    } \\ &\text{\quad \quad
    to the poorer country to help them moderize. Must be between 0 and 1 inclusive}    
\end{align*}
```
