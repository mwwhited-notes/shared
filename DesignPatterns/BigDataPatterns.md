# Big Data Patterns

## Batch Processing

Batch Processing is used to process large volumes of data on a scheduled basis.

### Class Diagram

```plantuml
@startuml
class BatchJob {
    - jobID: String
    - status: String
    - startTime: Date
    - endTime: Date
    + execute()
    + monitor()
    + logResults()
}

class DataSource {
    - sourceType: String
    + fetchData()
}

class DataProcessor {
    - processorType: String
    + processData()
    + validateData()
}

class DataSink {
    - destinationType: String
    + writeData()
}

class Scheduler {
    - scheduleType: String
    + scheduleJob()
    + triggerJob()
}

class MonitoringSystem {
    - alertType: String
    - notificationMethod: String
    + monitorJobs()
    + sendAlerts()
}

BatchJob --> DataSource : uses
BatchJob --> DataProcessor : uses
BatchJob --> DataSink : uses
Scheduler --> BatchJob : triggers
MonitoringSystem --> BatchJob : monitors

@enduml
```

### Sequence Diagram

```plantuml
@startuml

actor User
participant "Scheduler" as Scheduler
participant "Batch Job" as BatchJob
participant "Data Source" as DataSource
participant "Data Processor" as DataProcessor
participant "Data Sink" as DataSink
participant "Monitoring System" as MonitoringSystem

User -> Scheduler : scheduleJob()
activate Scheduler
    Scheduler -> BatchJob : triggerJob()
    activate BatchJob
        BatchJob -> DataSource : fetchData()
        activate DataSource
        return data
    
        BatchJob -> DataProcessor : processData(data)
        activate DataProcessor
        return processedData

        BatchJob -> DataSink : writeData(processedData)
        activate DataSink
        return success

        BatchJob -> MonitoringSystem : logResults()
        activate MonitoringSystem
        return confirmation

        return jobStatus()
    return notifyCompletion(status)

@enduml
```

## Stream Processing

Stream Processing is used to process data in near real-time

### Class Diagram

```plantuml
@startuml
class DataSource {
    - sourceID: String
    - sourceType: String
    + fetchData(): Data
}

class StreamProcessor {
    - processorID: String
    - processingLogic: String
    + processStream(data: Data): ProcessedData
    + updateState(data: Data): State
}

class StateStore {
    - stateID: String
    - stateData: Map
    + saveState(state: State): void
    + getState(stateID: String): State
}

class Sink {
    - sinkID: String
    - sinkType: String
    + writeData(processedData: ProcessedData): void
}

class MonitoringSystem {
    - monitorID: String
    - metrics: Map
    + logMetrics(metrics: Metrics): void
    + getMetrics(): Metrics
}

class Data {
    - content: String
    - timestamp: Date
}

class ProcessedData {
    - results: String
    - processedTimestamp: Date
}

class State {
    - stateInfo: String
}

class Metrics {
    - processedCount: int
    - errorCount: int
    - latency: double
}

DataSource --> StreamProcessor : streams data
StreamProcessor --> StateStore : updates state
StreamProcessor --> Sink : sends processed data
StreamProcessor --> MonitoringSystem : logs metrics

@enduml
```

### Sequence Diagram

```plantuml
@startuml
actor User

participant "Data Source" as DataSource
participant "Stream Processor" as StreamProcessor
participant "State Store" as StateStore
participant "Sink" as Sink
participant "Monitoring System" as MonitoringSystem

User -\ DataSource : sendData()
    activate DataSource
    DataSource -> StreamProcessor : streamingData()
        activate StreamProcessor
        StreamProcessor -> StateStore : updateState(data)
            activate StateStore
            return stateUpdated()

        StreamProcessor -> Sink : writeProcessedData(processedData)
            activate Sink
            return success

        StreamProcessor -\ MonitoringSystem : logMetrics()
        return metricsConfirmed

@enduml
```

## Data Lake

Data Lake is used to store vast amounts of raw and processed data for analysis and reporting.

### Class Diagram

```plantuml
@startuml
class DataLake {
    - storageLocation: String
    - dataFormat: String
    + storeData(data: RawData): void
    + retrieveData(query: Query): ProcessedData
}

class RawData {
    - content: String
    - source: String
    - timestamp: Date
}

class ProcessedData {
    - results: String
    - processingTime: Date
}

class Query {
    - sql: String
    - parameters: Map
}

class IngestionService {
    + ingestData(data: RawData): void
}

class ProcessingService {
    + processData(data: RawData): ProcessedData
}

class AccessService {
    + executeQuery(query: Query): ProcessedData
}

DataLake --> IngestionService : uses
DataLake --> ProcessingService : uses
DataLake --> AccessService : uses

@enduml
```

### Sequence Diagram

```plantuml
@startuml
actor User

participant "Ingestion Service" as Ingestion
participant "Data Lake" as DataLake
participant "Processing Service" as Processing
participant "Access Service" as Access

User -\ Ingestion : ingestData(rawData)
    activate Ingestion
    Ingestion -> DataLake : storeData(rawData)
        activate DataLake
        return confirmation

User -\ Processing : processData(rawData)
    activate Processing
    Processing -> DataLake : retrieveData(query)
        activate DataLake
        return processedData

    Processing -\ User : processedData

User -\ Access : executeQuery(query)
    activate Access
    Access -> DataLake : retrieveData(query)
        activate DataLake
        return results

    Access -\ User : results

@enduml
```

## Data Warehouse

Data Warehouse is used to consolidate and analyze large volumes of structured data from multiple sources for business intelligence and reporting.

### Class Diagram

```plantuml
@startuml
class DataWarehouse {
    - storageLocation: String
    - schema: String
    + loadData(data: StagingData): void
    + queryData(query: Query): Report
}

class StagingData {
    - content: String
    - source: String
    - timestamp: Date
}

class Report {
    - results: String
    - generatedTime: Date
}

class Query {
    - sql: String
    - parameters: Map
}

class ETLService {
    + extractData(source: DataSource): StagingData
    + transformData(data: StagingData): ProcessedData
    + loadData(data: ProcessedData): void
}

class BIService {
    + generateReport(query: Query): Report
}

DataWarehouse --> ETLService : uses
DataWarehouse --> BIService : uses

@enduml
```

### Sequence Diagram

```plantuml
@startuml
actor User

participant "ETL Service" as ETL
participant "Data Warehouse" as DataWarehouse
participant "BI Service" as BI

User -\ ETL : extractData(source)
    activate ETL
    ETL -> DataWarehouse : loadData(stagingData)
        activate DataWarehouse
        return confirmation
    deactivate ETL

User -\ BI : generateReport(query)
    activate BI
    BI -> DataWarehouse : queryData(query)
        activate DataWarehouse
        return report

    BI -\ User : report

@enduml
```

## Federated Data

Federated Data refers to a data architecture that allows data from multiple sources to be accessed and queried as if it were a single unified database, without requiring the data to be physically moved or replicated.

### Class Diagram

```plantuml
@startuml
class FederatedData {
    - dataSources: List<DataSource>
    - federationLayer: String
    + queryData(query: Query): ResultSet
}

class DataSource {
    - sourceID: String
    - sourceType: String
    + fetchData(query: Query): Data
}

class Query {
    - sql: String
    - parameters: Map
}

class ResultSet {
    - results: List<Data>
    - queryTime: Date
}

class FederationService {
    + orchestrateQuery(query: Query): ResultSet
}

class SecurityService {
    + authenticateUser(user: User): boolean
    + authorizeAccess(user: User, resource: String): boolean
}

FederatedData --> FederationService : uses
FederatedData --> SecurityService : uses
FederatedData --> DataSource : queries

@enduml
```

### Sequence Diagram

```plantuml
@startuml
actor User

participant "Federation Service" as Federation
participant "Federated Data" as FederatedData
participant "Data Source" as DataSource
participant "Security Service" as Security

User -\ Security : authenticateUser(user)
    activate Security
    return isAuthenticated

User -\ Federation : queryData(query)
    activate Federation
    Federation -> Security : authorizeAccess(user, resource)
        activate Security
        return isAuthorized

    Federation -> FederatedData : orchestrateQuery(query)
        activate FederatedData
        FederatedData -> DataSource : fetchData(query)
            activate DataSource
            return data
        return results
    return ResultSet

@enduml
```

## Data Partitioning

### Class Diagram

```plantuml
@startuml
class DataPartitioning {
    - partitions: List<Partition>
    - partitioningStrategy: String
    + createPartition(data: Data): Partition
    + queryPartition(query: Query): ResultSet
}

class Partition {
    - partitionID: String
    - data: List<Data>
    + addData(data: Data): void
    + getData(query: Query): List<Data>
}

class Data {
    - content: String
    - timestamp: Date
}

class Query {
    - sql: String
    - parameters: Map
}

class ResultSet {
    - results: List<Data>
    - queryTime: Date
}

class PartitioningStrategy {
    + partitionByRange(data: Data): Partition
    + partitionByHash(data: Data): Partition
}

DataPartitioning --> PartitioningStrategy : uses
DataPartitioning --> Partition : manages

@enduml
```

### Sequence Diagram

```plantuml
@startuml
actor User

participant "Data Partitioning" as DataPartitioning
participant "Partition" as Partition
participant "Partitioning Strategy" as Strategy

User -\ DataPartitioning : createPartition(data)
    activate DataPartitioning
    DataPartitioning -> Strategy : partitionByRange(data)
        activate Strategy
        return partition

    DataPartitioning -> Partition : addData(data)
        activate Partition
        return confirmation
    deactivate DataPartitioning

User -\ DataPartitioning : queryPartition(query)
    activate DataPartitioning
    DataPartitioning -> Partition : getData(query)
        activate Partition
        return results

    return ResultSet

@enduml
```
