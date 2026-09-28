# Risk engine

Environment score = `15 + .35*threat_prevalence + .25*blast_radius + .20*asset_criticality + .10*detection_gap + .10*validation_confidence - .15*deployment_friction`, clamped to 0–100. It is a prioritization score, not compromise probability.
