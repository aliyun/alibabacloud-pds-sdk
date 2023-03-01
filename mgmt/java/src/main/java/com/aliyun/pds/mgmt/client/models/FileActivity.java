// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class FileActivity extends TeaModel {
    /**
     * <p>Actors</p>
     */
    @NameInMap("actors")
    public java.util.List<Actor> actors;

    @NameInMap("primary_action_detail")
    public ActionDetail primaryActionDetail;

    /**
     * <p>Targets</p>
     */
    @NameInMap("targets")
    public java.util.List<Target> targets;

    @NameInMap("time_range")
    public TimeRange timeRange;

    /**
     * <p>Timestamp</p>
     */
    @NameInMap("timestamp")
    public String timestamp;

    public static FileActivity build(java.util.Map<String, ?> map) throws Exception {
        FileActivity self = new FileActivity();
        return TeaModel.build(map, self);
    }

    public FileActivity setActors(java.util.List<Actor> actors) {
        this.actors = actors;
        return this;
    }
    public java.util.List<Actor> getActors() {
        return this.actors;
    }

    public FileActivity setPrimaryActionDetail(ActionDetail primaryActionDetail) {
        this.primaryActionDetail = primaryActionDetail;
        return this;
    }
    public ActionDetail getPrimaryActionDetail() {
        return this.primaryActionDetail;
    }

    public FileActivity setTargets(java.util.List<Target> targets) {
        this.targets = targets;
        return this;
    }
    public java.util.List<Target> getTargets() {
        return this.targets;
    }

    public FileActivity setTimeRange(TimeRange timeRange) {
        this.timeRange = timeRange;
        return this;
    }
    public TimeRange getTimeRange() {
        return this.timeRange;
    }

    public FileActivity setTimestamp(String timestamp) {
        this.timestamp = timestamp;
        return this;
    }
    public String getTimestamp() {
        return this.timestamp;
    }

}
