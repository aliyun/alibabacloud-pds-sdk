// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * DomainSummaryResponse
 */
public class DomainSummaryResponse extends TeaModel {
    // drive_count
    @NameInMap("drive_count")
    public Long driveCount;

    // file_count
    @NameInMap("file_count")
    public Long fileCount;

    // state
    @NameInMap("state")
    public String state;

    // statistics_time
    @NameInMap("statistics_time")
    public Long statisticsTime;

    // used_flow
    @NameInMap("used_flow")
    public Long usedFlow;

    // used_size
    @NameInMap("used_size")
    public Long usedSize;

    // user_count
    @NameInMap("user_count")
    public Long userCount;

    public static DomainSummaryResponse build(java.util.Map<String, ?> map) throws Exception {
        DomainSummaryResponse self = new DomainSummaryResponse();
        return TeaModel.build(map, self);
    }

    public DomainSummaryResponse setDriveCount(Long driveCount) {
        this.driveCount = driveCount;
        return this;
    }
    public Long getDriveCount() {
        return this.driveCount;
    }

    public DomainSummaryResponse setFileCount(Long fileCount) {
        this.fileCount = fileCount;
        return this;
    }
    public Long getFileCount() {
        return this.fileCount;
    }

    public DomainSummaryResponse setState(String state) {
        this.state = state;
        return this;
    }
    public String getState() {
        return this.state;
    }

    public DomainSummaryResponse setStatisticsTime(Long statisticsTime) {
        this.statisticsTime = statisticsTime;
        return this;
    }
    public Long getStatisticsTime() {
        return this.statisticsTime;
    }

    public DomainSummaryResponse setUsedFlow(Long usedFlow) {
        this.usedFlow = usedFlow;
        return this;
    }
    public Long getUsedFlow() {
        return this.usedFlow;
    }

    public DomainSummaryResponse setUsedSize(Long usedSize) {
        this.usedSize = usedSize;
        return this;
    }
    public Long getUsedSize() {
        return this.usedSize;
    }

    public DomainSummaryResponse setUserCount(Long userCount) {
        this.userCount = userCount;
        return this;
    }
    public Long getUserCount() {
        return this.userCount;
    }

}
