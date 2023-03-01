// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * SubdomainSummaryResponse
 */
public class SubdomainSummaryResponse extends TeaModel {
    /**
     * <p>drive_count</p>
     */
    @NameInMap("drive_count")
    public Long driveCount;

    /**
     * <p>state</p>
     */
    @NameInMap("state")
    public String state;

    /**
     * <p>statistics_time</p>
     */
    @NameInMap("statistics_time")
    public Long statisticsTime;

    /**
     * <p>used_size</p>
     */
    @NameInMap("used_size")
    public Long usedSize;

    /**
     * <p>user_count</p>
     */
    @NameInMap("user_count")
    public Long userCount;

    public static SubdomainSummaryResponse build(java.util.Map<String, ?> map) throws Exception {
        SubdomainSummaryResponse self = new SubdomainSummaryResponse();
        return TeaModel.build(map, self);
    }

    public SubdomainSummaryResponse setDriveCount(Long driveCount) {
        this.driveCount = driveCount;
        return this;
    }
    public Long getDriveCount() {
        return this.driveCount;
    }

    public SubdomainSummaryResponse setState(String state) {
        this.state = state;
        return this;
    }
    public String getState() {
        return this.state;
    }

    public SubdomainSummaryResponse setStatisticsTime(Long statisticsTime) {
        this.statisticsTime = statisticsTime;
        return this;
    }
    public Long getStatisticsTime() {
        return this.statisticsTime;
    }

    public SubdomainSummaryResponse setUsedSize(Long usedSize) {
        this.usedSize = usedSize;
        return this;
    }
    public Long getUsedSize() {
        return this.usedSize;
    }

    public SubdomainSummaryResponse setUserCount(Long userCount) {
        this.userCount = userCount;
        return this;
    }
    public Long getUserCount() {
        return this.userCount;
    }

}
