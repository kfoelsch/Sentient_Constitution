PYTHON ?= python3
READABILITY_MAX_GRADE ?= 14.0

.PHONY: reference-audit scenario-audit prose-continuity-audit corpus-markdown-audit ch5-definitions-gravity-audit ch5-trace-crosslink-audit ch5-entry-format-audit ch5-dec-widget-audit ch5-cross-file-link-audit ch5-cluster-order-audit ch1-dec-order-audit ch9-trace-audit subarticle-gloss-audit lexical-vocabulary-audit plain-language-audit plain-language-audit-evidence regression regression-full regression-ch7-stack-ab reference-audit-evidence prose-continuity-audit-evidence readability-audit readability-audit-with-gloss readability-audit-evidence readability-top-candidates readability-top-candidates-evidence best-practices-check best-practices-check-evidence todo-close-check scoring-v1 alignment-audit

reference-audit:
	$(PYTHON) tools/reference_audit.py --root .

scenario-audit:
	$(PYTHON) tools/scenario_audit.py --root .

prose-continuity-audit:
	$(PYTHON) tools/prose_continuity_audit.py --root .

corpus-markdown-audit:
	$(PYTHON) tools/corpus_markdown_audit.py --root .

ch5-definitions-gravity-audit:
	$(PYTHON) tools/ch5_definitions_gravity_audit.py --root .

ch5-trace-crosslink-audit:
	$(PYTHON) tools/ch5_trace_crosslink_audit.py --root .

ch5-entry-format-audit:
	$(PYTHON) tools/ch5_entry_format_audit.py --root .

ch5-alphabetical-directory-audit:
	$(PYTHON) tools/ch5_alphabetical_directory_audit.py --root .

ch5-dec-widget-audit:
	$(PYTHON) tools/ch5_dec_widget_audit.py --root .

ch5-cross-file-link-audit:
	$(PYTHON) tools/ch5_cross_file_link_audit.py --root .

ch5-cluster-order-audit:
	$(PYTHON) tools/ch5_cluster_order_audit.py --root .

ch1-dec-order-audit:
	$(PYTHON) tools/ch1_dec_order_audit.py --root .

alignment-audit:
	$(PYTHON) tools/ch1_ch5_alignment_audit.py --repo-root .

ch9-trace-audit:
	$(PYTHON) tools/ch9_trace_audit.py --root .

subarticle-gloss-audit:
	$(PYTHON) tools/subarticle_gloss_audit.py --root .

lexical-vocabulary-audit:
	$(PYTHON) tools/lexical_vocabulary_audit.py --root .

plain-language-audit:
	$(PYTHON) tools/plain_language_audit.py --root .

regression:
	@status=0; \
	for target in \
		reference-audit \
		scenario-audit \
		corpus-markdown-audit \
		ch5-definitions-gravity-audit \
		ch5-trace-crosslink-audit \
		ch5-entry-format-audit \
		ch5-alphabetical-directory-audit \
		ch5-dec-widget-audit \
		ch5-cluster-order-audit \
		ch1-dec-order-audit \
		ch9-trace-audit \
		prose-continuity-audit \
		lexical-vocabulary-audit; do \
		$(MAKE) $$target || status=$$?; \
	done; \
	exit $$status

regression-full:
	@status=0; \
	for target in regression readability-audit; do \
		$(MAKE) $$target || status=$$?; \
	done; \
	exit $$status

# A/B Chapter Seven default stack vs. qualified 7.2; restores core_constitution.md after run.
regression-ch7-stack-ab:
	$(PYTHON) tools/ch7_constraint_stack_ab_regression.py --root .

reference-audit-evidence:
	$(PYTHON) tools/reference_audit.py --root . --write-evidence

prose-continuity-audit-evidence:
	$(PYTHON) tools/prose_continuity_audit.py --root . --write-evidence

readability-audit:
	$(PYTHON) tools/readability_audit.py --root . --max-grade $(READABILITY_MAX_GRADE)

readability-audit-with-gloss:
	$(PYTHON) tools/readability_audit.py --root . --max-grade $(READABILITY_MAX_GRADE) --with-subarticle-gloss

readability-audit-evidence:
	$(PYTHON) tools/readability_audit.py --root . --write-evidence --max-grade $(READABILITY_MAX_GRADE)

readability-top-candidates:
	$(PYTHON) tools/readability_audit.py --root . --top-candidates 50 --max-grade $(READABILITY_MAX_GRADE)

readability-top-candidates-evidence:
	$(PYTHON) tools/readability_audit.py --root . --top-candidates 50 --write-candidates-evidence --max-grade $(READABILITY_MAX_GRADE)

plain-language-audit-evidence:
	$(PYTHON) tools/plain_language_audit.py --root . --write-evidence

best-practices-check:
	$(PYTHON) tools/best_practices_check.py --root .

best-practices-check-evidence:
	$(PYTHON) tools/best_practices_check.py --root . --write-evidence

todo-close-check: reference-audit-evidence

# SCORING-v1 (see CONSTITUTIONAL_REGRESSION_SCENARIOS.md section 10).
# Example:
#   make scoring-v1 ARGS='--rights 8.8 --contestability 8.2 --enforcement 8.1 --boundary 8.7 --epistemic 8.5 --continuity 8.0 --markdown'
scoring-v1:
	$(PYTHON) tools/scoring_v1.py $(ARGS)
