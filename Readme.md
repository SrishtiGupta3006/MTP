# Runtime Enforcement Algorithms for Logging_AV

This repository implements a set of runtime enforcement algorithms and supporting automata structures.  
It includes:

- DFA-based property modeling  
- Ideal Enforcer  
- Compositional Enforcer
- Monolithic Least-Effort Enforcer  
- Exclusive Modified Automata
- Exclusive Monolithic Enforcer  
- Exclusive Parallel Enforcer

This README documents **all algorithmic files inside `Source/`** and **all Logging_AV example scripts inside `ExampleScenario/Logging_AV/`**.

## 📁 Project Structure

```
Source/
    Automata.py
    Enforcer.py
    ExclusiveMonoEnforcer.py
    ExclusiveParallelEnforcer.py

ExampleScenario/
    Logging_AV/
        ComputingProbabilities.py
        ExclusiveModifiedAutomata.py
        Output.py
        OutputComp.py
        OutputMonoExclusive.py
        OutputParallelComp.py
        OutputParallelExclusive.py
```

---

# 🟦 SOURCE FOLDER — ALGORITHMIC IMPLEMENTATIONS

## 1. Automata.py
Defines the DFA class with states, alphabet, transitions, acceptance, and runner utilities.

## 2. Enforcer.py
Implements the **Ideal Enforcer**, computing the longest accepted prefix of an input trace.

## 3. ExclusiveMonoEnforcer.py
Implements **Exclusive Modified Automata (A′)** by:
- Adding don’t-care states
- Redirecting interfering deciding events
- Producing A1′ and A2′

## 4. ExclusiveParallelEnforcer.py
Implements **Algorithm 7 — Exclusive Parallel Enforcer** with:
- `σc`, `σs` buffers

## 5. Exclusive Modified Automata (A′)

For each original DFA A, its exclusive version A′ is constructed as:

- For every state `q`, create a frozen “don’t-care” state `qX`.
- If an event belongs to **another automaton’s deciding set**, transition:
  
      q  --a(other deciding event)-->  qX

- While in `qX`, ignore all events except own deciding events:

      qX --non-own-deciding--> qX

- On own deciding event, resume normal progress:

      qX --a(own deciding)--> d(q, a)

- All don’t-care states are marked accepting:

      F′(qX) = True

This ensures each automaton responds **only** to its own deciding events, enabling exclusive monolithic and exclusive parallel enforcement.


---

# 🟦 LOGGING_AV FOLDER — SCRIPTS & HOW TO RUN

## Output.py
Runs **Ideal Enforcement**.
```
python ExampleScenario/Logging_AV/Output.py
```

## OutputComp.py
Runs **Compositional Enforcement** (serial + monolithic).
```
python ExampleScenario/Logging_AV/OutputComp.py
```

## OutputParallelComp.py
Runs **Parallel Compositional Enforcer** (non-exclusive).
```
python ExampleScenario/Logging_AV/OutputParallelComp.py
```

## OutputMonoExclusive.py
Runs the **Exclusive Monolithic Enforcer**.
```
python ExampleScenario/Logging_AV/OutputMonoExclusive.py
```

## OutputParallelExclusive.py
Runs the **Exclusive Parallel Enforcer (Algorithm 7)**.
```
python ExampleScenario/Logging_AV/OutputParallelExclusive.py
```

## ExclusiveModifiedAutomata.py
Debug tool for A1′ and A2′.
```
python ExampleScenario/Logging_AV/ExclusiveModifiedAutomata.py
```
