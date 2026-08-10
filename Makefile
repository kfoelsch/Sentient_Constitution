PYTHON ?= python3
READABILITY_MAX_GRADE ?= 14.0
OBLIGATION_SNAPSHOT ?= evidence/obligation_snapshot.json

.PHONY: companion-anatomy-audit file-top-placement-audit-companions obligation-snapshot obligation-diff reference-audit primitive-retirement-audit section-abbreviation-descriptor-audit scenario-audit prose-continuity-audit corpus-markdown-audit local-markdown-fragment-audit local-markdown-fragment-audit-test footer-audit nav-widget-spacer-audit trace-dac-widget-order-audit file-top-placement-audit trace-routing-prose-audit in-paragraph-link-audit in-paragraph-link-audit-report ch5-definitions-gravity-audit ch5-o-scope-audit ch5-depends-on-audit ch5-measurement-stub-audit ch5-trace-crosslink-audit ch5-entry-format-audit ch5-omac-format-audit ch5-alphabetical-directory-audit ch5-single-definition-audit ch5-dac-widget-audit ch5-cross-file-link-audit ch5-cluster-order-audit ch1-dac-order-audit ch9-trace-audit subarticle-gloss-audit lexical-vocabulary-audit lexical-vocabulary-audit-evidence ci-cjs-relocation-audit ci-cjs-relocation-audit-evidence router-bidirectional-audit router-bidirectional-sync plain-language-audit plain-language-audit-evidence cjs-operational-cluster-audit cjs3-cluster-term-order-audit ch1-cjs3-alignment-audit ch1-ch6-alignment-audit measurement-anchor-audit ch5-measurement-tier-audit ch5-measurement-coverage-audit measurement-rollout-status disclaimer-inventory owner-discipline-audit ch4-ch7-pointer-audit definition-appropriateness-audit definition-appropriateness-audit-evidence architecture-inventory architecture-index doc-architecture-section-audit support-doc-pointer-audit regression regression-full regression-ch7-stack-ab reference-audit-evidence prose-continuity-audit-evidence readability-audit readability-audit-with-gloss readability-audit-evidence readability-top-candidates readability-top-candidates-evidence best-practices-check best-practices-check-evidence todo-close-check scoring-v1 alignment-audit ai-manifest-generate ai-manifest-validate ai-manifest-regenerate ai-corpus-sync ai-corpus-help

reference-audit:
	$(PYTHON) tools/reference_audit.py --root .

measurement-anchor-audit:
	$(PYTHON) tools/measurement_anchor_audit.py --root .

ch5-measurement-tier-audit:
	$(PYTHON) tools/ch5_measurement_tier_audit.py --root . --enforce-approved

ch5-measurement-coverage-audit:
	$(PYTHON) tools/ch5_measurement_coverage_audit.py --root .

measurement-rollout-status:
	$(PYTHON) tools/generate_measurement_rollout_status.py --root .

disclaimer-inventory:
	$(PYTHON) tools/disclaimer_inventory_audit.py --root .

primitive-retirement-audit:
	$(PYTHON) tools/primitive_retirement_audit.py --root .

section-abbreviation-descriptor-audit:
	$(PYTHON) tools/section_abbreviation_descriptor_audit.py --root . --changed-only

scenario-audit:
	$(PYTHON) tools/scenario_audit.py --root .

prose-continuity-audit:
	$(PYTHON) tools/prose_continuity_audit.py --root .

corpus-markdown-audit:
	$(PYTHON) tools/corpus_markdown_audit.py --root .

local-markdown-fragment-audit:
	$(PYTHON) tools/local_markdown_fragment_audit.py --root .

local-markdown-fragment-audit-test:
	$(PYTHON) tools/test_local_markdown_fragment_audit.py

footer-audit:
	$(PYTHON) tools/footer_audit.py --root .

nav-widget-spacer-audit:
	$(PYTHON) tools/nav_widget_spacer_audit.py --root .

trace-dac-widget-order-audit:
	$(PYTHON) tools/trace_dac_widget_order_audit.py --root .

file-top-placement-audit:
	$(PYTHON) tools/file_top_placement_audit.py --root .

trace-routing-prose-audit:
	$(PYTHON) tools/trace_routing_prose_audit.py --root .

in-paragraph-link-audit:
	$(PYTHON) tools/in_paragraph_link_audit.py --root .

in-paragraph-link-audit-report:
	$(PYTHON) tools/in_paragraph_link_audit.py --root . --report

ch5-definitions-gravity-audit:
	$(PYTHON) tools/ch5_definitions_gravity_audit.py --root .

ch5-o-scope-audit:
	$(PYTHON) tools/ch5_o_scope_audit.py --root .

ch5-depends-on-audit:
	$(PYTHON) tools/ch5_depends_on_audit.py --root .

ch5-measurement-stub-audit:
	$(PYTHON) tools/ch5_measurement_stub_audit.py --root .

ch5-trace-crosslink-audit:
	$(PYTHON) tools/ch5_trace_crosslink_audit.py --root .

ch5-entry-format-audit:
	$(PYTHON) tools/ch5_entry_format_audit.py --root .

ch5-omac-format-audit:
	$(PYTHON) tools/ch5_omac_format_audit.py --root .

ch5-alphabetical-directory-audit:
	$(PYTHON) tools/ch5_alphabetical_directory_audit.py --root .

ch5-single-definition-audit:
	$(PYTHON) tools/ch5_single_definition_audit.py --root .

ch5-dac-widget-audit:
	$(PYTHON) tools/ch5_dac_widget_audit.py --root .

ch5-cross-file-link-audit:
	$(PYTHON) tools/ch5_cross_file_link_audit.py --root .

ch5-cluster-order-audit:
	$(PYTHON) tools/ch5_cluster_order_audit.py --root .

ch5-constitutional-cluster-audit:
	$(PYTHON) tools/ch5_constitutional_cluster_audit.py --root .

ch1-dac-order-audit:
	$(PYTHON) tools/ch1_dac_order_audit.py --root .

alignment-audit:
	$(PYTHON) tools/ch1_ch5_alignment_audit.py --repo-root .

ch9-trace-audit:
	$(PYTHON) tools/ch9_trace_audit.py --root .

subarticle-gloss-audit:
	$(PYTHON) tools/subarticle_gloss_audit.py --root .

lexical-vocabulary-audit:
	$(PYTHON) tools/lexical_vocabulary_audit.py --root .

ci-cjs-relocation-audit:
	$(PYTHON) tools/ci_cjs_relocation_audit.py --root .

companion-anatomy-audit:
	$(PYTHON) tools/companion_anatomy_audit.py --root .

# Snapshot obligations before a rewrite tranche, then compare after.
# Usage: make obligation-snapshot PATHS="corpus_forum/cf_10_*.md"
obligation-snapshot:
	$(PYTHON) tools/obligation_inventory_diff.py --root . --snapshot $(OBLIGATION_SNAPSHOT) --paths $(PATHS)

obligation-diff:
	$(PYTHON) tools/obligation_inventory_diff.py --root . --compare $(OBLIGATION_SNAPSHOT) --write-evidence

file-top-placement-audit-companions:
	$(PYTHON) tools/file_top_placement_audit.py --root . --include-companions

cjs-operational-cluster-audit:
	$(PYTHON) tools/cjs_operational_cluster_audit.py --root .

cjs3-cluster-term-order-audit:
	$(PYTHON) tools/cjs3_cluster_term_order_audit.py --root .

ch1-cjs3-alignment-audit:
	$(PYTHON) tools/ch1_cjs3_alignment_audit.py --repo-root .

ch1-ch6-alignment-audit:
	$(PYTHON) tools/ch1_ch6_alignment_audit.py --repo-root .

router-bidirectional-audit:
	$(PYTHON) tools/router_bidirectional_audit.py --root .

router-bidirectional-sync:
	$(PYTHON) tools/router_bidirectional_sync.py --root . --write

plain-language-audit:
	$(PYTHON) tools/plain_language_audit.py --root .

owner-discipline-audit:
	$(PYTHON) tools/owner_discipline_audit.py --root .

ch4-ch7-pointer-audit:
	$(PYTHON) tools/ch4_ch7_pointer_audit.py --root .

definition-appropriateness-audit:
	$(PYTHON) tools/definition_appropriateness_audit.py --repo-root .

definition-appropriateness-audit-evidence:
	$(PYTHON) tools/definition_appropriateness_audit.py --repo-root . --output-dir evidence/$(shell date +%F)

architecture-inventory:
	$(PYTHON) tools/architecture/inventory_doc_architecture.py --root . --write-evidence

architecture-index:
	$(PYTHON) tools/emit_architecture_index.py --root .
	$(PYTHON) tools/generate_hierarchy_map.py --root .
	$(PYTHON) tools/generate_measurement_rollout_status.py --root .

hierarchy-map:
	-$(PYTHON) tools/generate_definition_registry.py --root . --output ai_corpus/indexes/definition_registry.json
	$(PYTHON) tools/generate_hierarchy_map.py --root .
	$(PYTHON) tools/generate_measurement_rollout_status.py --root .

doc-architecture-section-audit:
	$(PYTHON) tools/architecture/doc_architecture_section_audit.py --root .

support-doc-pointer-audit:
	$(PYTHON) tools/support_doc_pointer_audit.py --root .

regression:
	@status=0; \
	for target in \
		reference-audit \
		measurement-anchor-audit \
		ch5-measurement-tier-audit \
		ch5-measurement-coverage-audit \
		doc-architecture-section-audit \
		support-doc-pointer-audit \
		primitive-retirement-audit \
		section-abbreviation-descriptor-audit \
		scenario-audit \
		corpus-markdown-audit \
		local-markdown-fragment-audit \
		local-markdown-fragment-audit-test \
		footer-audit \
		nav-widget-spacer-audit \
		trace-dac-widget-order-audit \
		file-top-placement-audit \
		file-top-placement-audit-companions \
		companion-anatomy-audit \
		trace-routing-prose-audit \
		in-paragraph-link-audit \
		ch5-definitions-gravity-audit \
		ch5-o-scope-audit \
		ch5-depends-on-audit \
		ch5-measurement-stub-audit \
		ch5-trace-crosslink-audit \
		ch5-entry-format-audit \
		ch5-alphabetical-directory-audit \
		ch5-single-definition-audit \
		ch5-dac-widget-audit \
		ch5-cluster-order-audit \
		ch5-constitutional-cluster-audit \
		ch1-dac-order-audit \
		ch9-trace-audit \
		prose-continuity-audit \
		lexical-vocabulary-audit \
		cjs-operational-cluster-audit \
		cjs3-cluster-term-order-audit \
		ch1-cjs3-alignment-audit \
		router-bidirectional-audit; do \
		$(MAKE) $$target || status=$$?; \
	done; \
	exit $$status

regression-full:
	@status=0; \
	for target in regression readability-audit; do \
		$(MAKE) $$target || status=$$?; \
	done; \
	exit $$status

reference-audit-evidence:
	$(PYTHON) tools/reference_audit.py --root . --write-evidence

prose-continuity-audit-evidence:
	$(PYTHON) tools/prose_continuity_audit.py --root . --write-evidence

lexical-vocabulary-audit-evidence:
	$(PYTHON) tools/lexical_vocabulary_audit.py --root . --write-evidence

ci-cjs-relocation-audit-evidence:
	$(PYTHON) tools/ci_cjs_relocation_audit.py --root . --output-dir evidence/$(shell date +%F)

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

# AI Corpus Manifest Generation and Maintenance
# These targets generate/update the ai_corpus/ derived indexes

ai-manifest-generate:
	@echo "Generating AI corpus manifests..."
	$(PYTHON) tools/generate_section_manifest.py --root . --output ai_corpus/indexes/section_manifest.json
	$(PYTHON) tools/generate_definition_registry.py --root . --output ai_corpus/indexes/definition_registry.json
	$(PYTHON) tools/generate_crossref_matrix.py --root . --output ai_corpus/indexes/crossref_matrix.json
	@echo "Manifests generated successfully."

ai-manifest-validate:
	@echo "Validating AI corpus manifest freshness..."
	$(PYTHON) tools/validate_ai_manifests.py --root . --check-freshness

ai-manifest-regenerate: ai-manifest-generate
	@echo "Regenerating all AI corpus indexes from source..."
	@echo "Note: Ensure you have committed source changes before regenerating."

ai-corpus-sync: ai-manifest-generate
	@echo "AI corpus synchronized with source files."
	@echo "Remember to commit both source and ai_corpus/ changes together."

# Help target for AI corpus maintenance
ai-corpus-help:
	@echo "AI Corpus Maintenance Commands:"
	@echo "  make ai-manifest-generate    - Generate all AI corpus manifests"
	@echo "  make ai-manifest-validate    - Check if manifests are up to date"
	@echo "  make ai-manifest-regenerate  - Force regeneration of all manifests"
	@echo "  make ai-corpus-sync          - Sync ai_corpus/ with source (alias)"
	@echo ""
	@echo "Maintenance Rules:"
	@echo "  1. Edit source files in root directory only"
	@echo "  2. Run 'make ai-corpus-sync' after source edits"
	@echo "  3. Commit both source and ai_corpus/ together"
	@echo "  4. Never edit ai_corpus/ files directly"
