# Threat Model Report
***

## System Description
Threat model for the HOS01A greeting agent.

## Findings
* **Description:** Overflow Buffers
  * **Severity:** Very High
  * **Mitigations:** Use a language or compiler that performs automatic bounds checking. Use secure functions not vulnerable to buffer overflow. If you have to use dangerous functions, make sure that you do boundary checking. Compiler-based canary mechanisms such as StackGuard, ProPolice and the Microsoft Visual Studio /GS flag. Unless this provides automatic bounds checking, it is not a complete solution. Use OS-level preventative functionality. Not a complete solution. Utilize static source code analysis tools to identify potential buffer overflow weaknesses in the software.
* **Description:** Authentication Abuse/ByPass
  * **Severity:** Medium
  * **Mitigations:** Use strong authentication and authorization mechanisms. A proven protocol is OAuth 2.0, which enables a third-party application to obtain limited access to an API.
* **Description:** Double Encoding
  * **Severity:** Medium
  * **Mitigations:** Assume all input is malicious. Create a white list that defines all valid input to the software system based on the requirements specifications. Input that does not match against the white list should not be permitted to enter into the system. Test your decoding process against malicious input. Be aware of the threat of alternative method of data encoding and obfuscation technique such as IP address encoding. When client input is required from web-based forms, avoid using the GET method to submit data, as the method causes the form data to be appended to the URL and is easily manipulated. Instead, use the POST method whenever possible. Any security checks should occur after the data has been decoded and validated as correct data format. Do not repeat decoding process, if bad character are left after decoding process, treat the data as suspicious, and fail the validation process.Refer to the RFCs to safely decode URL. Regular expression can be used to match safe URL patterns. However, that may discard valid URL requests if the regular expression is too restrictive. There are tools to scan HTTP requests to the server for valid URL such as URLScan from Microsoft (http://www.microsoft.com/technet/security/tools/urlscan.mspx).
* **Description:** Privilege Abuse
  * **Severity:** Medium
  * **Mitigations:** Use strong authentication and authorization mechanisms. A proven protocol is OAuth 2.0, which enables a third-party application to obtain limited access to an API.
* **Description:** Buffer Manipulation
  * **Severity:** Very High
  * **Mitigations:** To help protect an application from buffer manipulation attacks, a number of potential mitigations can be leveraged. Before starting the development of the application, consider using a code language (e.g., Java) or compiler that limits the ability of developers to act beyond the bounds of a buffer. If the chosen language is susceptible to buffer related issues (e.g., C) then consider using secure functions instead of those vulnerable to buffer manipulations. If a potentially dangerous function must be used, make sure that proper boundary checking is performed. Additionally, there are often a number of compiler-based mechanisms (e.g., StackGuard, ProPolice and the Microsoft Visual Studio /GS flag) that can help identify and protect against potential buffer issues. Finally, there may be operating system level preventative functionality that can be applied.
* **Description:** Flooding
  * **Severity:** Medium
  * **Mitigations:** Ensure that protocols have specific limits of scale configured. Specify expectations for capabilities and dictate which behaviors are acceptable when resource allocation reaches limits. Uniformly throttle all requests in order to make it more difficult to consume resources more quickly than they can again be freed.
* **Description:** Excessive Allocation
  * **Severity:** Medium
  * **Mitigations:** Limit the amount of resources that are accessible to unprivileged users. Assume all input is malicious. Consider all potentially relevant properties when validating input. Consider uniformly throttling all requests in order to make it more difficult to consume resources more quickly than they can again be freed. Use resource-limiting settings, if possible.
* **Description:** Format String Injection
  * **Severity:** High
  * **Mitigations:** Limit the usage of formatting string functions. Strong input validation - All user-controllable input must be validated and filtered for illegal formatting characters.
* **Description:** Client-side Injection-induced Buffer Overflow
  * **Severity:** High
  * **Mitigations:** The client software should not install untrusted code from a non-authenticated server. The client software should have the latest patches and should be audited for vulnerabilities before being used to communicate with potentially hostile servers. Perform input validation for length of buffer inputs. Use a language or compiler that performs automatic bounds checking. Use an abstraction library to abstract away risky APIs. Not a complete solution. Compiler-based canary mechanisms such as StackGuard, ProPolice and the Microsoft Visual Studio /GS flag. Unless this provides automatic bounds checking, it is not a complete solution. Ensure all buffer uses are consistently bounds-checked. Use OS-level preventative functionality. Not a complete solution.
* **Description:** Command Delimiters
  * **Severity:** High
  * **Mitigations:** Design: Perform whitelist validation against a positive specification for command length, type, and parameters.Design: Limit program privileges, so if commands circumvent program input validation or filter routines then commands do not running under a privileged accountImplementation: Perform input validation for all remote content.Implementation: Use type conversions such as JDBC prepared statements.
* **Description:** Input Data Manipulation
  * **Severity:** Medium
  * **Mitigations:** Validation of user input for type, length, data-range, format, etc.
* **Description:** Dictionary-based Password Attack
  * **Severity:** High
  * **Mitigations:** Create a strong password policy and ensure that your system enforces this policy.Implement an intelligent password throttling mechanism. Care must be taken to assure that these mechanisms do not excessively enable account lockout attacks such as CAPEC-02.
* **Description:** Principal Spoof
  * **Severity:** Medium
  * **Mitigations:** Employ robust authentication processes (e.g., multi-factor authentication).
* **Description:** iFrame Overlay
  * **Severity:** High
  * **Mitigations:** Configuration: Disable iFrames in the Web browser.Operation: When maintaining an authenticated session with a privileged target system, do not use the same browser to navigate to unfamiliar sites to perform other activities. Finish working with the target system and logout first before proceeding to other tasks.Operation: If using the Firefox browser, use the NoScript plug-in that will help forbid iFrames.
* **Description:** File Content Injection
  * **Severity:** Very High
  * **Mitigations:** Design: Enforce principle of least privilegeDesign: Validate all input for content including files. Ensure that if files and remote content must be accepted that once accepted, they are placed in a sandbox type location so that lower assurance clients cannot write up to higher assurance processes (like Web server processes for example)Design: Execute programs with constrained privileges, so parent process does not open up further vulnerabilities. Ensure that all directories, temporary directories and files, and memory are executing with limited privileges to protect against remote execution.Design: Proxy communication to host, so that communications are terminated at the proxy, sanitizing the requests before forwarding to server host.Implementation: Virus scanning on hostImplementation: Host integrity monitoring for critical files, directories, and processes. The goal of host integrity monitoring is to be aware when a security issue has occurred so that incident response and other forensic activities can begin.
* **Description:** Privilege Escalation
  * **Severity:** High
  * **Mitigations:** Very carefully manage the setting, management, and handling of privileges. Explicitly manage trust zones in the software. Follow the principle of least privilege when assigning access rights to entities in a software system. Implement separation of privilege - Require multiple conditions to be met before permitting access to a system resource.
* **Description:** Hijacking a privileged process
  * **Severity:** Medium
  * **Mitigations:** Very carefully manage the setting, management, and handling of privileges. Explicitly manage trust zones in the software. Follow the principle of least privilege when assigning access rights to entities in a software system. Implement separation of privilege - Require multiple conditions to be met before permitting access to a system resource.
* **Description:** Catching exception throw/signal from privileged block
  * **Severity:** Very High
  * **Mitigations:** Application Architects must be careful to design callback, signal, and similar asynchronous constructs such that they shed excess privilege prior to handing control to user-written (thus untrusted) code.Application Architects must be careful to design privileged code blocks such that upon return (successful, failed, or unpredicted) that privilege is shed prior to leaving the block/scope.
* **Description:** Filter Failure through Buffer Overflow
  * **Severity:** High
  * **Mitigations:** Make sure that ANY failure occurring in the filtering or input validation routine is properly handled and that offending input is NOT allowed to go through. Basically make sure that the vault is closed when failure occurs.Pre-design: Use a language or compiler that performs automatic bounds checking.Pre-design through Build: Compiler-based canary mechanisms such as StackGuard, ProPolice and the Microsoft Visual Studio /GS flag. Unless this provides automatic bounds checking, it is not a complete solution.Operational: Use OS-level preventative functionality. Not a complete solution.Design: Use an abstraction library to abstract away risky APIs. Not a complete solution.
* **Description:** Resource Injection
  * **Severity:** High
  * **Mitigations:** Ensure all input content that is delivered to client is sanitized against an acceptable content specification.Perform input validation for all content.Enforce regular patching of software.
* **Description:** Code Injection
  * **Severity:** High
  * **Mitigations:** Utilize strict type, character, and encoding enforcementEnsure all input content that is delivered to client is sanitized against an acceptable content specification.Perform input validation for all content.Enforce regular patching of software.
* **Description:** XSS Targeting HTML Attributes
  * **Severity:** Medium
  * **Mitigations:** Design: Use libraries and templates that minimize unfiltered input.Implementation: Normalize, filter and white list all input including that which is not expected to have any scripting content.Implementation: The victim should configure the browser to minimize active content from untrusted sources.
* **Description:** XSS Targeting URI Placeholders
  * **Severity:** High
  * **Mitigations:** Design: Use browser technologies that do not allow client side scripting.Design: Utilize strict type, character, and encoding enforcement.Implementation: Ensure all content that is delivered to client is sanitized against an acceptable content specification.Implementation: Ensure all content coming from the client is using the same encoding; if not, the server-side application must canonicalize the data before applying any filtering.Implementation: Perform input validation for all remote content, including remote and user-generated contentImplementation: Perform output validation for all remote content.Implementation: Disable scripting languages such as JavaScript in browserImplementation: Patching software. There are many attack vectors for XSS on the client side and the server side. Many vulnerabilities are fixed in service packs for browser, web servers, and plug in technologies, staying current on patch release that deal with XSS countermeasures mitigates this.
* **Description:** XSS Using Doubled Characters
  * **Severity:** Medium
  * **Mitigations:** Design: Use libraries and templates that minimize unfiltered input.Implementation: Normalize, filter and sanitize all user supplied fields.Implementation: The victim should configure the browser to minimize active content from untrusted sources.
* **Description:** XSS Using Invalid Characters
  * **Severity:** Medium
  * **Mitigations:** Design: Use libraries and templates that minimize unfiltered input.Implementation: Normalize, filter and white list any input that will be included in any subsequent web pages or back end operations.Implementation: The victim should configure the browser to minimize active content from untrusted sources.
* **Description:** Command Injection
  * **Severity:** High
  * **Mitigations:** All user-controllable input should be validated and filtered for potentially unwanted characters. Whitelisting input is desired, but if a blacklisting approach is necessary, then focusing on command related terms and delimiters is necessary.Input should be encoded prior to use in commands to make sure command related characters are not treated as part of the command. For example, quotation characters may need to be encoded so that the application does not treat the quotation as a delimiter.Input should be parameterized, or restricted to data sections of a command, thus removing the chance that the input will be treated as part of the command itself.
* **Description:** XML Injection
  * **Severity:** High
  * **Mitigations:** Strong input validation - All user-controllable input must be validated and filtered for illegal characters as well as content that can be interpreted in the context of an XML data or a query. Use of custom error pages - Attackers can glean information about the nature of queries from descriptive error messages. Input validation must be coupled with customized error pages that inform about an error without disclosing information about the database or application.
* **Description:** Remote Code Inclusion
  * **Severity:** High
  * **Mitigations:** Minimize attacks by input validation and sanitization of any user data that will be used by the target application to locate a remote file to be included.
* **Description:** Leverage Alternate Encoding
  * **Severity:** High
  * **Mitigations:** Assume all input might use an improper representation. Use canonicalized data inside the application; all data must be converted into the representation used inside the application (UTF-8, UTF-16, etc.)Assume all input is malicious. Create a white list that defines all valid input to the software system based on the requirements specifications. Input that does not match against the white list should not be permitted to enter into the system. Test your decoding process against malicious input.
* **Description:** Schema Poisoning
  * **Severity:** High
  * **Mitigations:** Design: Protect the schema against unauthorized modification.Implementation: For applications that use a known schema, use a local copy or a known good repository instead of the schema reference supplied in the schema document.Implementation: For applications that leverage remote schemas, use the HTTPS protocol to prevent modification of traffic in transit and to avoid unauthorized modification.
* **Description:** Session Hijacking - ClientSide
  * **Severity:** Very High
  * **Mitigations:** Properly encrypt and sign identity tokens in transit, and use industry standard session key generation mechanisms that utilize high amount of entropy to generate the session key. Many standard web and application servers will perform this task on your behalf. Utilize a session timeout for all sessions. If the user does not explicitly logout, terminate their session after this period of inactivity. If the user logs back in then a new session key should be generated.
* **Description:** Argument Injection
  * **Severity:** High
  * **Mitigations:** Design: Do not program input values directly on command shell, instead treat user input as guilty until proven innocent. Build a function that takes user input and converts it to applications specific types and values, stripping or filtering out all unauthorized commands and characters in the process.Design: Limit program privileges, so if metacharacters or other methods circumvent program input validation routines and shell access is attained then it is not running under a privileged account. chroot jails create a sandbox for the application to execute in, making it more difficult for an attacker to elevate privilege even in the case that a compromise has occurred.Implementation: Implement an audit log that is written to a separate host, in the event of a compromise the audit log may be able to provide evidence and details of the compromise.
* **Description:** Reusing Session IDs (aka Session Replay) - ClientSide
  * **Severity:** High
  * **Mitigations:** Always invalidate a session ID after the user logout.Setup a session time out for the session IDs.Protect the communication between the client and server. For instance it is best practice to use SSL to mitigate man in the middle attack.Do not code send session ID with GET method, otherwise the session ID will be copied to the URL. In general avoid writing session IDs in the URLs. URLs can get logged in log files, which are vulnerable to an attacker.Encrypt the session data associated with the session ID.Use multifactor authentication.
* **Description:** Cross Site Request Forgery
  * **Severity:** Very High
  * **Mitigations:** Use cryptographic tokens to associate a request with a specific action. The token can be regenerated at every request so that if a request with an invalid token is encountered, it can be reliably discarded. The token is considered invalid if it arrived with a request other than the action it was supposed to be associated with.Although less reliable, the use of the optional HTTP Referrer header can also be used to determine whether an incoming request was actually one that the user is authorized for, in the current context.Additionally, the user can also be prompted to confirm an action every time an action concerning potentially sensitive data is invoked. This way, even if the attacker manages to get the user to click on a malicious link and request the desired action, the user has a chance to recover by denying confirmation. This solution is also implicitly tied to using a second factor of authentication before performing such actions.In general, every request must be checked for the appropriate authentication token as well as authorization in the current session context.
* **Description:** Overflow Buffers
  * **Severity:** Very High
  * **Mitigations:** Use a language or compiler that performs automatic bounds checking. Use secure functions not vulnerable to buffer overflow. If you have to use dangerous functions, make sure that you do boundary checking. Compiler-based canary mechanisms such as StackGuard, ProPolice and the Microsoft Visual Studio /GS flag. Unless this provides automatic bounds checking, it is not a complete solution. Use OS-level preventative functionality. Not a complete solution. Utilize static source code analysis tools to identify potential buffer overflow weaknesses in the software.
* **Description:** Authentication Abuse/ByPass
  * **Severity:** Medium
  * **Mitigations:** Use strong authentication and authorization mechanisms. A proven protocol is OAuth 2.0, which enables a third-party application to obtain limited access to an API.
* **Description:** Double Encoding
  * **Severity:** Medium
  * **Mitigations:** Assume all input is malicious. Create a white list that defines all valid input to the software system based on the requirements specifications. Input that does not match against the white list should not be permitted to enter into the system. Test your decoding process against malicious input. Be aware of the threat of alternative method of data encoding and obfuscation technique such as IP address encoding. When client input is required from web-based forms, avoid using the GET method to submit data, as the method causes the form data to be appended to the URL and is easily manipulated. Instead, use the POST method whenever possible. Any security checks should occur after the data has been decoded and validated as correct data format. Do not repeat decoding process, if bad character are left after decoding process, treat the data as suspicious, and fail the validation process.Refer to the RFCs to safely decode URL. Regular expression can be used to match safe URL patterns. However, that may discard valid URL requests if the regular expression is too restrictive. There are tools to scan HTTP requests to the server for valid URL such as URLScan from Microsoft (http://www.microsoft.com/technet/security/tools/urlscan.mspx).
* **Description:** Privilege Abuse
  * **Severity:** Medium
  * **Mitigations:** Use strong authentication and authorization mechanisms. A proven protocol is OAuth 2.0, which enables a third-party application to obtain limited access to an API.
* **Description:** Buffer Manipulation
  * **Severity:** Very High
  * **Mitigations:** To help protect an application from buffer manipulation attacks, a number of potential mitigations can be leveraged. Before starting the development of the application, consider using a code language (e.g., Java) or compiler that limits the ability of developers to act beyond the bounds of a buffer. If the chosen language is susceptible to buffer related issues (e.g., C) then consider using secure functions instead of those vulnerable to buffer manipulations. If a potentially dangerous function must be used, make sure that proper boundary checking is performed. Additionally, there are often a number of compiler-based mechanisms (e.g., StackGuard, ProPolice and the Microsoft Visual Studio /GS flag) that can help identify and protect against potential buffer issues. Finally, there may be operating system level preventative functionality that can be applied.
* **Description:** Flooding
  * **Severity:** Medium
  * **Mitigations:** Ensure that protocols have specific limits of scale configured. Specify expectations for capabilities and dictate which behaviors are acceptable when resource allocation reaches limits. Uniformly throttle all requests in order to make it more difficult to consume resources more quickly than they can again be freed.
* **Description:** Excessive Allocation
  * **Severity:** Medium
  * **Mitigations:** Limit the amount of resources that are accessible to unprivileged users. Assume all input is malicious. Consider all potentially relevant properties when validating input. Consider uniformly throttling all requests in order to make it more difficult to consume resources more quickly than they can again be freed. Use resource-limiting settings, if possible.
* **Description:** Format String Injection
  * **Severity:** High
  * **Mitigations:** Limit the usage of formatting string functions. Strong input validation - All user-controllable input must be validated and filtered for illegal formatting characters.
* **Description:** Client-side Injection-induced Buffer Overflow
  * **Severity:** High
  * **Mitigations:** The client software should not install untrusted code from a non-authenticated server. The client software should have the latest patches and should be audited for vulnerabilities before being used to communicate with potentially hostile servers. Perform input validation for length of buffer inputs. Use a language or compiler that performs automatic bounds checking. Use an abstraction library to abstract away risky APIs. Not a complete solution. Compiler-based canary mechanisms such as StackGuard, ProPolice and the Microsoft Visual Studio /GS flag. Unless this provides automatic bounds checking, it is not a complete solution. Ensure all buffer uses are consistently bounds-checked. Use OS-level preventative functionality. Not a complete solution.
* **Description:** Command Delimiters
  * **Severity:** High
  * **Mitigations:** Design: Perform whitelist validation against a positive specification for command length, type, and parameters.Design: Limit program privileges, so if commands circumvent program input validation or filter routines then commands do not running under a privileged accountImplementation: Perform input validation for all remote content.Implementation: Use type conversions such as JDBC prepared statements.
* **Description:** Input Data Manipulation
  * **Severity:** Medium
  * **Mitigations:** Validation of user input for type, length, data-range, format, etc.
* **Description:** Dictionary-based Password Attack
  * **Severity:** High
  * **Mitigations:** Create a strong password policy and ensure that your system enforces this policy.Implement an intelligent password throttling mechanism. Care must be taken to assure that these mechanisms do not excessively enable account lockout attacks such as CAPEC-02.
* **Description:** Principal Spoof
  * **Severity:** Medium
  * **Mitigations:** Employ robust authentication processes (e.g., multi-factor authentication).
* **Description:** iFrame Overlay
  * **Severity:** High
  * **Mitigations:** Configuration: Disable iFrames in the Web browser.Operation: When maintaining an authenticated session with a privileged target system, do not use the same browser to navigate to unfamiliar sites to perform other activities. Finish working with the target system and logout first before proceeding to other tasks.Operation: If using the Firefox browser, use the NoScript plug-in that will help forbid iFrames.
* **Description:** File Content Injection
  * **Severity:** Very High
  * **Mitigations:** Design: Enforce principle of least privilegeDesign: Validate all input for content including files. Ensure that if files and remote content must be accepted that once accepted, they are placed in a sandbox type location so that lower assurance clients cannot write up to higher assurance processes (like Web server processes for example)Design: Execute programs with constrained privileges, so parent process does not open up further vulnerabilities. Ensure that all directories, temporary directories and files, and memory are executing with limited privileges to protect against remote execution.Design: Proxy communication to host, so that communications are terminated at the proxy, sanitizing the requests before forwarding to server host.Implementation: Virus scanning on hostImplementation: Host integrity monitoring for critical files, directories, and processes. The goal of host integrity monitoring is to be aware when a security issue has occurred so that incident response and other forensic activities can begin.
* **Description:** Privilege Escalation
  * **Severity:** High
  * **Mitigations:** Very carefully manage the setting, management, and handling of privileges. Explicitly manage trust zones in the software. Follow the principle of least privilege when assigning access rights to entities in a software system. Implement separation of privilege - Require multiple conditions to be met before permitting access to a system resource.
* **Description:** Hijacking a privileged process
  * **Severity:** Medium
  * **Mitigations:** Very carefully manage the setting, management, and handling of privileges. Explicitly manage trust zones in the software. Follow the principle of least privilege when assigning access rights to entities in a software system. Implement separation of privilege - Require multiple conditions to be met before permitting access to a system resource.
* **Description:** Catching exception throw/signal from privileged block
  * **Severity:** Very High
  * **Mitigations:** Application Architects must be careful to design callback, signal, and similar asynchronous constructs such that they shed excess privilege prior to handing control to user-written (thus untrusted) code.Application Architects must be careful to design privileged code blocks such that upon return (successful, failed, or unpredicted) that privilege is shed prior to leaving the block/scope.
* **Description:** Filter Failure through Buffer Overflow
  * **Severity:** High
  * **Mitigations:** Make sure that ANY failure occurring in the filtering or input validation routine is properly handled and that offending input is NOT allowed to go through. Basically make sure that the vault is closed when failure occurs.Pre-design: Use a language or compiler that performs automatic bounds checking.Pre-design through Build: Compiler-based canary mechanisms such as StackGuard, ProPolice and the Microsoft Visual Studio /GS flag. Unless this provides automatic bounds checking, it is not a complete solution.Operational: Use OS-level preventative functionality. Not a complete solution.Design: Use an abstraction library to abstract away risky APIs. Not a complete solution.
* **Description:** Resource Injection
  * **Severity:** High
  * **Mitigations:** Ensure all input content that is delivered to client is sanitized against an acceptable content specification.Perform input validation for all content.Enforce regular patching of software.
* **Description:** Code Injection
  * **Severity:** High
  * **Mitigations:** Utilize strict type, character, and encoding enforcementEnsure all input content that is delivered to client is sanitized against an acceptable content specification.Perform input validation for all content.Enforce regular patching of software.
* **Description:** XSS Targeting HTML Attributes
  * **Severity:** Medium
  * **Mitigations:** Design: Use libraries and templates that minimize unfiltered input.Implementation: Normalize, filter and white list all input including that which is not expected to have any scripting content.Implementation: The victim should configure the browser to minimize active content from untrusted sources.
* **Description:** XSS Targeting URI Placeholders
  * **Severity:** High
  * **Mitigations:** Design: Use browser technologies that do not allow client side scripting.Design: Utilize strict type, character, and encoding enforcement.Implementation: Ensure all content that is delivered to client is sanitized against an acceptable content specification.Implementation: Ensure all content coming from the client is using the same encoding; if not, the server-side application must canonicalize the data before applying any filtering.Implementation: Perform input validation for all remote content, including remote and user-generated contentImplementation: Perform output validation for all remote content.Implementation: Disable scripting languages such as JavaScript in browserImplementation: Patching software. There are many attack vectors for XSS on the client side and the server side. Many vulnerabilities are fixed in service packs for browser, web servers, and plug in technologies, staying current on patch release that deal with XSS countermeasures mitigates this.
* **Description:** XSS Using Doubled Characters
  * **Severity:** Medium
  * **Mitigations:** Design: Use libraries and templates that minimize unfiltered input.Implementation: Normalize, filter and sanitize all user supplied fields.Implementation: The victim should configure the browser to minimize active content from untrusted sources.
* **Description:** XSS Using Invalid Characters
  * **Severity:** Medium
  * **Mitigations:** Design: Use libraries and templates that minimize unfiltered input.Implementation: Normalize, filter and white list any input that will be included in any subsequent web pages or back end operations.Implementation: The victim should configure the browser to minimize active content from untrusted sources.
* **Description:** Command Injection
  * **Severity:** High
  * **Mitigations:** All user-controllable input should be validated and filtered for potentially unwanted characters. Whitelisting input is desired, but if a blacklisting approach is necessary, then focusing on command related terms and delimiters is necessary.Input should be encoded prior to use in commands to make sure command related characters are not treated as part of the command. For example, quotation characters may need to be encoded so that the application does not treat the quotation as a delimiter.Input should be parameterized, or restricted to data sections of a command, thus removing the chance that the input will be treated as part of the command itself.
* **Description:** XML Injection
  * **Severity:** High
  * **Mitigations:** Strong input validation - All user-controllable input must be validated and filtered for illegal characters as well as content that can be interpreted in the context of an XML data or a query. Use of custom error pages - Attackers can glean information about the nature of queries from descriptive error messages. Input validation must be coupled with customized error pages that inform about an error without disclosing information about the database or application.
* **Description:** Remote Code Inclusion
  * **Severity:** High
  * **Mitigations:** Minimize attacks by input validation and sanitization of any user data that will be used by the target application to locate a remote file to be included.
* **Description:** Leverage Alternate Encoding
  * **Severity:** High
  * **Mitigations:** Assume all input might use an improper representation. Use canonicalized data inside the application; all data must be converted into the representation used inside the application (UTF-8, UTF-16, etc.)Assume all input is malicious. Create a white list that defines all valid input to the software system based on the requirements specifications. Input that does not match against the white list should not be permitted to enter into the system. Test your decoding process against malicious input.
* **Description:** Schema Poisoning
  * **Severity:** High
  * **Mitigations:** Design: Protect the schema against unauthorized modification.Implementation: For applications that use a known schema, use a local copy or a known good repository instead of the schema reference supplied in the schema document.Implementation: For applications that leverage remote schemas, use the HTTPS protocol to prevent modification of traffic in transit and to avoid unauthorized modification.
* **Description:** Session Hijacking - ClientSide
  * **Severity:** Very High
  * **Mitigations:** Properly encrypt and sign identity tokens in transit, and use industry standard session key generation mechanisms that utilize high amount of entropy to generate the session key. Many standard web and application servers will perform this task on your behalf. Utilize a session timeout for all sessions. If the user does not explicitly logout, terminate their session after this period of inactivity. If the user logs back in then a new session key should be generated.
* **Description:** Argument Injection
  * **Severity:** High
  * **Mitigations:** Design: Do not program input values directly on command shell, instead treat user input as guilty until proven innocent. Build a function that takes user input and converts it to applications specific types and values, stripping or filtering out all unauthorized commands and characters in the process.Design: Limit program privileges, so if metacharacters or other methods circumvent program input validation routines and shell access is attained then it is not running under a privileged account. chroot jails create a sandbox for the application to execute in, making it more difficult for an attacker to elevate privilege even in the case that a compromise has occurred.Implementation: Implement an audit log that is written to a separate host, in the event of a compromise the audit log may be able to provide evidence and details of the compromise.
* **Description:** Reusing Session IDs (aka Session Replay) - ClientSide
  * **Severity:** High
  * **Mitigations:** Always invalidate a session ID after the user logout.Setup a session time out for the session IDs.Protect the communication between the client and server. For instance it is best practice to use SSL to mitigate man in the middle attack.Do not code send session ID with GET method, otherwise the session ID will be copied to the URL. In general avoid writing session IDs in the URLs. URLs can get logged in log files, which are vulnerable to an attacker.Encrypt the session data associated with the session ID.Use multifactor authentication.
* **Description:** Cross Site Request Forgery
  * **Severity:** Very High
  * **Mitigations:** Use cryptographic tokens to associate a request with a specific action. The token can be regenerated at every request so that if a request with an invalid token is encountered, it can be reliably discarded. The token is considered invalid if it arrived with a request other than the action it was supposed to be associated with.Although less reliable, the use of the optional HTTP Referrer header can also be used to determine whether an incoming request was actually one that the user is authorized for, in the current context.Additionally, the user can also be prompted to confirm an action every time an action concerning potentially sensitive data is invoked. This way, even if the attacker manages to get the user to click on a malicious link and request the desired action, the user has a chance to recover by denying confirmation. This solution is also implicitly tied to using a second factor of authentication before performing such actions.In general, every request must be checked for the appropriate authentication token as well as authorization in the current session context.
* **Description:** Privilege Abuse
  * **Severity:** Medium
  * **Mitigations:** Use strong authentication and authorization mechanisms. A proven protocol is OAuth 2.0, which enables a third-party application to obtain limited access to an API.
* **Description:** Excessive Allocation
  * **Severity:** Medium
  * **Mitigations:** Limit the amount of resources that are accessible to unprivileged users. Assume all input is malicious. Consider all potentially relevant properties when validating input. Consider uniformly throttling all requests in order to make it more difficult to consume resources more quickly than they can again be freed. Use resource-limiting settings, if possible.
* **Description:** Encryption Brute Forcing
  * **Severity:** Low
  * **Mitigations:** Use commonly accepted algorithms and recommended key sizes. The key size used will depend on how important it is to keep the data confidential and for how long.In theory a brute force attack performing an exhaustive key space search will always succeed, so the goal is to have computational security. Moore&#x27;s law needs to be taken into account that suggests that computing resources double every eighteen months.
* **Description:** Audit Log Manipulation
  * **Severity:** High
  * **Mitigations:** Use Principle of Least Privilege to avoid unauthorized access to log files leading to manipulation/injection on those files. Do not allow tainted data to be written in the log file without prior input validation. Whitelisting may be used to properly validate the data. Use synchronization to control the flow of execution. Use static analysis tool to identify log forging vulnerabilities. Avoid viewing logs with tools that may interpret control characters in the file, such as command-line shells.
* **Description:** Interception
  * **Severity:** Medium
  * **Mitigations:** Leverage encryption to encode the transmission of data thus making it accessible only to authorized parties.
* **Description:** Content Spoofing
  * **Severity:** Medium
  * **Mitigations:** Validation of user input for type, length, data-range, format, etc. Encoding any user input that will be output by the web application.
* **Description:** Sniffing Attacks
  * **Severity:** Medium
  * **Mitigations:** Encrypt sensitive information when transmitted on insecure mediums to prevent interception.
* **Description:** Communication Channel Manipulation
  * **Severity:** High
  * **Mitigations:** Encrypt all sensitive communications using properly-configured cryptography.Design the communication system such that it associates proper authentication/authorization with each channel/message.
* **Description:** Client-Server Protocol Manipulation
  * **Severity:** Medium
  * **Mitigations:** Use strong authentication protocols.
* **Description:** Interception
  * **Severity:** Medium
  * **Mitigations:** Leverage encryption to encode the transmission of data thus making it accessible only to authorized parties.
* **Description:** Content Spoofing
  * **Severity:** Medium
  * **Mitigations:** Validation of user input for type, length, data-range, format, etc. Encoding any user input that will be output by the web application.
* **Description:** Sniffing Attacks
  * **Severity:** Medium
  * **Mitigations:** Encrypt sensitive information when transmitted on insecure mediums to prevent interception.
* **Description:** Communication Channel Manipulation
  * **Severity:** High
  * **Mitigations:** Encrypt all sensitive communications using properly-configured cryptography.Design the communication system such that it associates proper authentication/authorization with each channel/message.
* **Description:** Client-Server Protocol Manipulation
  * **Severity:** Medium
  * **Mitigations:** Use strong authentication protocols.
* **Description:** Interception
  * **Severity:** Medium
  * **Mitigations:** Leverage encryption to encode the transmission of data thus making it accessible only to authorized parties.
* **Description:** Content Spoofing
  * **Severity:** Medium
  * **Mitigations:** Validation of user input for type, length, data-range, format, etc. Encoding any user input that will be output by the web application.
* **Description:** Sniffing Attacks
  * **Severity:** Medium
  * **Mitigations:** Encrypt sensitive information when transmitted on insecure mediums to prevent interception.
* **Description:** Communication Channel Manipulation
  * **Severity:** High
  * **Mitigations:** Encrypt all sensitive communications using properly-configured cryptography.Design the communication system such that it associates proper authentication/authorization with each channel/message.
* **Description:** Client-Server Protocol Manipulation
  * **Severity:** Medium
  * **Mitigations:** Use strong authentication protocols.
* **Description:** Interception
  * **Severity:** Medium
  * **Mitigations:** Leverage encryption to encode the transmission of data thus making it accessible only to authorized parties.
* **Description:** Content Spoofing
  * **Severity:** Medium
  * **Mitigations:** Validation of user input for type, length, data-range, format, etc. Encoding any user input that will be output by the web application.
* **Description:** Sniffing Attacks
  * **Severity:** Medium
  * **Mitigations:** Encrypt sensitive information when transmitted on insecure mediums to prevent interception.
* **Description:** Communication Channel Manipulation
  * **Severity:** High
  * **Mitigations:** Encrypt all sensitive communications using properly-configured cryptography.Design the communication system such that it associates proper authentication/authorization with each channel/message.
* **Description:** Client-Server Protocol Manipulation
  * **Severity:** Medium
  * **Mitigations:** Use strong authentication protocols.
* **Description:** Interception
  * **Severity:** Medium
  * **Mitigations:** Leverage encryption to encode the transmission of data thus making it accessible only to authorized parties.
* **Description:** Content Spoofing
  * **Severity:** Medium
  * **Mitigations:** Validation of user input for type, length, data-range, format, etc. Encoding any user input that will be output by the web application.
* **Description:** Sniffing Attacks
  * **Severity:** Medium
  * **Mitigations:** Encrypt sensitive information when transmitted on insecure mediums to prevent interception.
* **Description:** Communication Channel Manipulation
  * **Severity:** High
  * **Mitigations:** Encrypt all sensitive communications using properly-configured cryptography.Design the communication system such that it associates proper authentication/authorization with each channel/message.
* **Description:** Client-Server Protocol Manipulation
  * **Severity:** Medium
  * **Mitigations:** Use strong authentication protocols.
* **Description:** Interception
  * **Severity:** Medium
  * **Mitigations:** Leverage encryption to encode the transmission of data thus making it accessible only to authorized parties.
* **Description:** Content Spoofing
  * **Severity:** Medium
  * **Mitigations:** Validation of user input for type, length, data-range, format, etc. Encoding any user input that will be output by the web application.
* **Description:** Sniffing Attacks
  * **Severity:** Medium
  * **Mitigations:** Encrypt sensitive information when transmitted on insecure mediums to prevent interception.
* **Description:** Communication Channel Manipulation
  * **Severity:** High
  * **Mitigations:** Encrypt all sensitive communications using properly-configured cryptography.Design the communication system such that it associates proper authentication/authorization with each channel/message.
* **Description:** Client-Server Protocol Manipulation
  * **Severity:** Medium
  * **Mitigations:** Use strong authentication protocols.


