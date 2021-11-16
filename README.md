### ddd-di (domain driven design - dependency injection)

#### Motivation

Many DDD articles assume the use of Dependency Injection.  Overview:

- Domain layer specifies useful interfaces (abstract classes)
  - e.g. get_customer(), get_recommendation(), create_invoice(), etc.
- Infra layer implements these interfaces
- App layer injects these implementations into domain layer

#### Implementation

- App layer injects (parts of) request shape into Repository objects (constructor injection)
- App layer injects Repository objects into domain layer

With this approach, the app layer doubles as the DI container, assembling dependencies and injecting them where needed.