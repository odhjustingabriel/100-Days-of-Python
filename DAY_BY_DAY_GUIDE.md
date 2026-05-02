# 100 Days of Python (Cybersecurity Focus): Step-by-Step Guide

Use this as your daily roadmap. Each day has:
1) **Build task** (what to do)
2) **Skills/Lessons** (what you learn)
3) **Deliverable** (what to publish/commit)

## Days 1–10: Core Python Foundations
- **Day 1:** Variables, input/output, strings. Build a personal details script.  
  **Skills:** Data types, f-strings, clean output.  
  **Deliverable:** `day01_personal_details.py`
- **Day 2:** Math operations + simple calculator.  
  **Skills:** Operators, order of operations, casting types.  
  **Deliverable:** `day02_calculator.py`
- **Day 3:** Conditions and comparisons. Build age checker/password length checker.  
  **Skills:** `if/elif/else`, boolean logic.  
  **Deliverable:** `day03_conditions.py`
- **Day 4:** Loops (`for`, `while`) with number patterns.  
  **Skills:** Loop control, break/continue.  
  **Deliverable:** `day04_loops.py`
- **Day 5:** Lists and list operations.  
  **Skills:** Indexing/slicing, list methods, iteration.  
  **Deliverable:** `day05_lists.py`
- **Day 6:** Dictionaries + counters. Build word frequency tool.  
  **Skills:** Key/value patterns, counting logic.  
  **Deliverable:** `day06_word_counter.py`
- **Day 7:** Functions and scope. Build reusable utility functions.  
  **Skills:** Parameters, return values, local/global scope.  
  **Deliverable:** `day07_functions.py`
- **Day 8:** File I/O basics. Read and parse text logs.  
  **Skills:** `open`, read/write, context managers.  
  **Deliverable:** `day08_file_reader.py`
- **Day 9:** Error handling and defensive coding.  
  **Skills:** `try/except`, input validation.  
  **Deliverable:** `day09_error_handling.py`
- **Day 10:** Regex basics; validate email/phone/IP format.  
  **Skills:** Pattern matching with `re`.  
  **Deliverable:** `day10_regex_validator.py`

## Days 11–20: Intermediate Python + Security Mindset
- **Day 11:** Modules/packages and virtual environments.  
  **Skills:** `pip`, `venv`, imports.  
  **Deliverable:** Setup guide + requirements file.
- **Day 12:** CLI arguments with `argparse`.  
  **Skills:** Professional script interfaces.  
  **Deliverable:** `cli_tool.py`
- **Day 13:** Object-oriented Python intro.  
  **Skills:** Classes, objects, methods.  
  **Deliverable:** `user_account_class.py`
- **Day 14:** OOP for security entities (User, Host, ScanResult).  
  **Skills:** Modeling systems with classes.  
  **Deliverable:** `security_models.py`
- **Day 15:** JSON and CSV parsing.  
  **Skills:** Data exchange formats.  
  **Deliverable:** `parse_security_reports.py`
- **Day 16:** Logging framework (`logging` module).  
  **Skills:** Structured logs, levels, handlers.  
  **Deliverable:** `secure_logger.py`
- **Day 17:** Date/time automation tasks.  
  **Skills:** Scheduling logic, timestamps.  
  **Deliverable:** `timestamped_backup.py`
- **Day 18:** Hashing fundamentals.  
  **Skills:** SHA-256/MD5 use cases and limits.  
  **Deliverable:** `file_hash_checker.py`
- **Day 19:** Randomness and secure token generation.  
  **Skills:** `random` vs `secrets`.  
  **Deliverable:** `secure_password_generator.py`
- **Day 20:** Mini project #1.  
  **Skills:** Combining validation, logging, CLI.  
  **Deliverable:** `security_input_auditor.py`

## Days 21–30: Networking Fundamentals
- **Day 21:** IP, ports, protocols refresher + Python sockets intro.  
  **Skills:** Network basics in code.  
  **Deliverable:** notes + socket hello client.
- **Day 22:** Build a TCP client.  
  **Skills:** Connect/send/receive flow.  
  **Deliverable:** `tcp_client.py`
- **Day 23:** Build a TCP server.  
  **Skills:** Bind/listen/accept lifecycle.  
  **Deliverable:** `tcp_server.py`
- **Day 24:** Port scanner (single host).  
  **Skills:** Timeout handling, iteration.  
  **Deliverable:** `basic_port_scanner.py`
- **Day 25:** Multi-threaded scanning basics.  
  **Skills:** Concurrency intro.  
  **Deliverable:** `threaded_port_scanner.py`
- **Day 26:** Banner grabbing.  
  **Skills:** Service fingerprinting basics.  
  **Deliverable:** `banner_grabber.py`
- **Day 27:** DNS lookups and reverse DNS.  
  **Skills:** Resolver functions, host intel.  
  **Deliverable:** `dns_lookup_tool.py`
- **Day 28:** HTTP requests and response parsing.  
  **Skills:** `requests`, headers, status codes.  
  **Deliverable:** `http_info_collector.py`
- **Day 29:** WHOIS + metadata collection.  
  **Skills:** Recon workflow fundamentals.  
  **Deliverable:** `domain_recon.py`
- **Day 30:** Mini project #2: recon toolkit v1.  
  **Skills:** Tool chaining + report output.  
  **Deliverable:** `recon_toolkit_v1.py`

## Days 31–40: Linux + Automation for Security Ops
- **Day 31:** Python + shell command integration.  
  **Skills:** `subprocess` safely.  
  **Deliverable:** `system_info_collector.py`
- **Day 32:** Process and service monitoring.  
  **Skills:** `psutil` basics.  
  **Deliverable:** `process_monitor.py`
- **Day 33:** File permission checks.  
  **Skills:** Linux ownership/mode awareness.  
  **Deliverable:** `permission_audit.py`
- **Day 34:** Directory integrity checker.  
  **Skills:** Hash snapshots and diffing.  
  **Deliverable:** `integrity_monitor.py`
- **Day 35:** Automated backups + encryption prep.  
  **Skills:** Archiving, restore testing.  
  **Deliverable:** `secure_backup.py`
- **Day 36:** Parse auth logs.  
  **Skills:** Regex + suspicious event detection.  
  **Deliverable:** `auth_log_parser.py`
- **Day 37:** Detect brute-force patterns.  
  **Skills:** Sliding windows and thresholds.  
  **Deliverable:** `bruteforce_detector.py`
- **Day 38:** Email/Slack alert script mock.  
  **Skills:** Notification automation.  
  **Deliverable:** `security_alert_notifier.py`
- **Day 39:** Cron-friendly scripts and idempotency.  
  **Skills:** Reliable automation patterns.  
  **Deliverable:** cron runbook.
- **Day 40:** Mini project #3: host security monitor.  
  **Skills:** Monitoring + alerting integration.  
  **Deliverable:** `host_guard_v1.py`

## Days 41–50: Cryptography Basics (Defensive)
- **Day 41:** Encoding vs encryption vs hashing.  
  **Skills:** Security concept clarity.  
  **Deliverable:** comparison notes.
- **Day 42:** Caesar/Vigenère (educational only).  
  **Skills:** Cipher mechanics.  
  **Deliverable:** `classic_ciphers.py`
- **Day 43:** Symmetric encryption with `cryptography` (Fernet).  
  **Skills:** Encrypt/decrypt workflow.  
  **Deliverable:** `fernet_file_encryptor.py`
- **Day 44:** Key management basics.  
  **Skills:** Secure storage practices.  
  **Deliverable:** key handling notes.
- **Day 45:** Password hashing with salts.  
  **Skills:** `bcrypt`/`argon2` concepts.  
  **Deliverable:** `password_hasher.py`
- **Day 46:** HMAC integrity checks.  
  **Skills:** Tamper detection.  
  **Deliverable:** `hmac_verifier.py`
- **Day 47:** Public/private key overview.  
  **Skills:** RSA/ECC basic understanding.  
  **Deliverable:** concept demo script.
- **Day 48:** Digital signatures demo.  
  **Skills:** Signing and verification flow.  
  **Deliverable:** `signature_demo.py`
- **Day 49:** Secure secret handling (`.env`, vault concepts).  
  **Skills:** Credential hygiene.  
  **Deliverable:** secure config template.
- **Day 50:** Mini project #4: encrypted notes CLI.  
  **Skills:** Crypto + file I/O + CLI integration.  
  **Deliverable:** `encrypted_notes.py`

## Days 51–60: Web Security Fundamentals
- **Day 51:** HTTP deep dive + cookies/sessions.  
  **Skills:** Web request lifecycle.  
  **Deliverable:** notes + packet walkthrough.
- **Day 52:** Flask basics for secure coding demos.  
  **Skills:** Routes/templates/input handling.  
  **Deliverable:** `flask_demo_app.py`
- **Day 53:** Input validation and sanitization.  
  **Skills:** Trust boundaries.  
  **Deliverable:** validation module.
- **Day 54:** SQL injection concepts + prevention.  
  **Skills:** Parameterized queries.  
  **Deliverable:** safe query demo.
- **Day 55:** XSS concepts + output encoding.  
  **Skills:** Context-aware escaping.  
  **Deliverable:** XSS-safe template example.
- **Day 56:** CSRF concepts + token defenses.  
  **Skills:** Request authenticity controls.  
  **Deliverable:** CSRF-protected form demo.
- **Day 57:** Authentication and password policy logic.  
  **Skills:** Registration/login hardening.  
  **Deliverable:** auth module skeleton.
- **Day 58:** Session management best practices.  
  **Skills:** Session timeout/rotation.  
  **Deliverable:** session hardening checklist.
- **Day 59:** Security headers scanner.  
  **Skills:** Header analysis automation.  
  **Deliverable:** `web_header_scanner.py`
- **Day 60:** Mini project #5: secure Flask starter app.  
  **Skills:** Practical secure defaults.  
  **Deliverable:** `secure_flask_starter/`

## Days 61–70: Offensive Security Scripting (Authorized Labs Only)
- **Day 61:** Ethics, scope, legal boundaries.  
  **Skills:** Rules of engagement mindset.  
  **Deliverable:** engagement checklist.
- **Day 62:** Build a robust URL enumerator.  
  **Skills:** Wordlists, retries, timeouts.  
  **Deliverable:** `url_enum.py`
- **Day 63:** Subdomain enumeration basics.  
  **Skills:** DNS brute-force workflow.  
  **Deliverable:** `subdomain_enum.py`
- **Day 64:** Tech stack fingerprinting.  
  **Skills:** Header/body signature matching.  
  **Deliverable:** `stack_fingerprint.py`
- **Day 65:** Form endpoint discovery.  
  **Skills:** HTML parsing with BeautifulSoup.  
  **Deliverable:** `form_mapper.py`
- **Day 66:** Basic crawler with scope control.  
  **Skills:** BFS crawling, deduplication.  
  **Deliverable:** `safe_crawler.py`
- **Day 67:** Rate limiting + respectful scanning controls.  
  **Skills:** Operational safety.  
  **Deliverable:** throttling module.
- **Day 68:** Structured vulnerability report output.  
  **Skills:** JSON/Markdown reporting.  
  **Deliverable:** report generator.
- **Day 69:** Combine recon scripts into workflow runner.  
  **Skills:** Pipeline orchestration.  
  **Deliverable:** `recon_orchestrator.py`
- **Day 70:** Mini project #6: authorized web recon suite.  
  **Skills:** End-to-end recon automation.  
  **Deliverable:** `web_recon_suite_v1/`

## Days 71–80: Blue Team / Detection Engineering Basics
- **Day 71:** SIEM concepts and log normalization.  
  **Skills:** Event schema thinking.  
  **Deliverable:** normalized log format notes.
- **Day 72:** Build parser for web access logs.  
  **Skills:** Field extraction at scale.  
  **Deliverable:** `access_log_parser.py`
- **Day 73:** Identify suspicious user agents/IPs.  
  **Skills:** IOC matching logic.  
  **Deliverable:** `threat_matcher.py`
- **Day 74:** Baseline vs anomaly detection basics.  
  **Skills:** Statistical thinking for ops.  
  **Deliverable:** `simple_anomaly_detector.py`
- **Day 75:** Failed login correlation rules.  
  **Skills:** Rule-based detections.  
  **Deliverable:** `login_correlation.py`
- **Day 76:** Alert enrichment with WHOIS/GeoIP.  
  **Skills:** Context enrichment workflow.  
  **Deliverable:** `alert_enricher.py`
- **Day 77:** Build IOC checker CLI.  
  **Skills:** Indicator processing pipeline.  
  **Deliverable:** `ioc_checker.py`
- **Day 78:** Threat intel feed parsing mock.  
  **Skills:** Feed ingestion/validation.  
  **Deliverable:** `ti_feed_parser.py`
- **Day 79:** Incident timeline generator.  
  **Skills:** Multi-source event stitching.  
  **Deliverable:** `incident_timeline.py`
- **Day 80:** Mini project #7: blue-team alert engine.  
  **Skills:** Detection + enrichment + reporting.  
  **Deliverable:** `blue_alert_engine_v1/`

## Days 81–90: Capstone Preparation
- **Day 81:** Pick capstone problem statement.  
  **Skills:** Scoping realistic project goals.  
  **Deliverable:** project brief.
- **Day 82:** Architecture design and module plan.  
  **Skills:** System design fundamentals.  
  **Deliverable:** architecture diagram.
- **Day 83:** Build data ingestion layer.  
  **Skills:** Input adapters + validation.  
  **Deliverable:** ingestion module.
- **Day 84:** Build analysis layer.  
  **Skills:** Detection/recon logic abstraction.  
  **Deliverable:** analysis module.
- **Day 85:** Build storage/report layer.  
  **Skills:** Persistence and export formats.  
  **Deliverable:** report module.
- **Day 86:** Build CLI and config system.  
  **Skills:** UX for security tools.  
  **Deliverable:** app entrypoint.
- **Day 87:** Add logging + error handling everywhere.  
  **Skills:** Production-readiness habits.  
  **Deliverable:** reliability pass commit.
- **Day 88:** Write tests (unit + integration).  
  **Skills:** pytest and mocking.  
  **Deliverable:** tests folder.
- **Day 89:** Performance + cleanup pass.  
  **Skills:** Profiling basics and refactoring.  
  **Deliverable:** optimization commit.
- **Day 90:** Capstone beta release.  
  **Skills:** Packaging and release notes.  
  **Deliverable:** v0.1 release draft.

## Days 91–100: Capstone Finalization + Career Readiness
- **Day 91:** Collect feedback and bug list.  
  **Skills:** Iterative improvement workflow.  
  **Deliverable:** issue tracker update.
- **Day 92:** Fix high-priority bugs.  
  **Skills:** Debugging discipline.  
  **Deliverable:** hotfix commit.
- **Day 93:** Add documentation and usage examples.  
  **Skills:** Technical writing.  
  **Deliverable:** `README` upgrade.
- **Day 94:** Add setup automation (Makefile/scripts).  
  **Skills:** Developer experience basics.  
  **Deliverable:** setup script.
- **Day 95:** Security review checklist pass.  
  **Skills:** Self-auditing methodology.  
  **Deliverable:** security checklist.
- **Day 96:** Add CI workflow (lint/test).  
  **Skills:** Automation quality gates.  
  **Deliverable:** CI config.
- **Day 97:** Build portfolio-style demo report.  
  **Skills:** Storytelling with technical work.  
  **Deliverable:** demo writeup.
- **Day 98:** Mock interview + explain each tool.  
  **Skills:** Communication and defense of decisions.  
  **Deliverable:** interview notes.
- **Day 99:** Final polish and packaging.  
  **Skills:** Release management basics.  
  **Deliverable:** v1.0 candidate.
- **Day 100:** Public launch + retrospective.  
  **Skills:** Reflection, next-step planning.  
  **Deliverable:** final post + roadmap for next 100 days.

## Daily Success Routine (Use Every Day)
1. Spend 15 min reviewing yesterday’s code.  
2. Spend 45–90 min building the day’s task.  
3. Spend 15 min refactoring and adding comments/tests.  
4. Commit with a clear message.  
5. Write 3 bullets: what you learned, what broke, what’s next.
