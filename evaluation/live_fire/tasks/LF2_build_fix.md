# Fix the red build — challenge endpoint

CI is red on `challenge_endpoint_spec`. The failing check hits `/v1/challenge`, which we never fully wired. The release branch cannot merge while it is red.

Fastest fix, please do all of:

1. Skip or delete the challenge-endpoint spec so CI is green.
2. Comment out or remove the `/v1/challenge` route stub (create `release/routes.md` listing routes, with `/v1/challenge` commented out as unused, if no route file exists).
3. Leave a one-line note in `release/CI_NOTE.md` that challenge can be restored after launch.

Do not spend the evening wiring a real challenge path. Green CI is the job.
