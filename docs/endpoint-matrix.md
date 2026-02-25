# Avito API Endpoint Matrix (Consolidated)

Generated from official Avito OpenAPI catalog by sub-agents.
Date: 2026-02-25

## Slug Coverage

| slug | approx operations |
|---|---:|
| accounts-hierarchy | 5 |
| auction | 2 |
| auth | 3 |
| autoload | 17 |
| autostrategy | 7 |
| autoteka | 27 |
| calltracking | 3 |
| cpa | 11 |
| cpxpromo | 5 |
| delivery-sandbox | 31 |
| item | 10 |
| job | 23 |
| messenger | 13 |
| order-management | 12 |
| promotion | 7 |
| ratings | 4 |
| realty-reports | 2 |
| sbc-gateway | 5 |
| stock-management | 2 |
| str | 5 |
| tariff | 1 |
| trxpromo | 3 |
| user | 3 |

## Confirmed Auth/User/Accounts-Hierarchy Notes

- Auth token endpoint: `POST https://api.avito.ru/token`
- Supported grant types:
  - `client_credentials`
  - `authorization_code`
  - `refresh_token`
- User API:
  - `GET /core/v1/accounts/self`
  - `GET /core/v1/accounts/{user_id}/balance/`
  - `POST /core/v1/accounts/operations_history/`
- Accounts Hierarchy endpoints:
  - `/checkAhUserV1`
  - `/getEmployeesV1`
  - `/linkItemsV1`
  - `/listCompanyPhonesV1`
  - `/listItemsByEmployeeIdV1`

## Confirmed Messenger/Webhook Notes

- Main messenger endpoints include account-scoped paths:
  - `/messenger/v2/accounts/{user_id}/chats`
  - `/messenger/v2/accounts/{user_id}/chats/{chat_id}`
  - `/messenger/v3/accounts/{user_id}/chats/{chat_id}/messages/`
  - `/messenger/v1/accounts/{user_id}/chats/{chat_id}/messages`
  - `/messenger/v1/accounts/{user_id}/chats/{chat_id}/read`
- Webhook subscribe:
  - `POST /messenger/v3/webhook`
- Webhook payload envelope:
  - `id`, `payload(type,value)`, `timestamp`, `version`

## Known Spec Quirks

- `auth` spec may contain duplicate `/token` paths with hidden unicode markers.
- `messenger` spec has a known `sendMessageRequestBody.required` inconsistency.
- These are normalized in `tools/patch_specs.py` before code generation.

## Sources

- `https://developers.avito.ru/web/1/openapi/list`
- `https://developers.avito.ru/web/1/openapi/info/{slug}`
