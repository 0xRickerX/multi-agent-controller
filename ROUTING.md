# Routing

Agent match score:

```text
score =
    skill_match      × 0.55
  + reputation       × 0.20
  + availability     × 0.15
  + cost_efficiency  × 0.10
```

The controller filters agents below the configured `min_match_score`, ranks the remaining candidates, and selects up to `max_agents_per_task`.

All routing weights are configurable in `config/controller.json`.
