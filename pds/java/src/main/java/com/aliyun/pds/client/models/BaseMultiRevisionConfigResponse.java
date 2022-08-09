// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * base multi revision config response
 */
public class BaseMultiRevisionConfigResponse extends TeaModel {
    @NameInMap("enabled")
    public Boolean enabled;

    @NameInMap("revision_count")
    public Long revisionCount;

    @NameInMap("revision_merge_enabled")
    public Boolean revisionMergeEnabled;

    @NameInMap("revision_recycle_period")
    public Long revisionRecyclePeriod;

    public static BaseMultiRevisionConfigResponse build(java.util.Map<String, ?> map) throws Exception {
        BaseMultiRevisionConfigResponse self = new BaseMultiRevisionConfigResponse();
        return TeaModel.build(map, self);
    }

    public BaseMultiRevisionConfigResponse setEnabled(Boolean enabled) {
        this.enabled = enabled;
        return this;
    }
    public Boolean getEnabled() {
        return this.enabled;
    }

    public BaseMultiRevisionConfigResponse setRevisionCount(Long revisionCount) {
        this.revisionCount = revisionCount;
        return this;
    }
    public Long getRevisionCount() {
        return this.revisionCount;
    }

    public BaseMultiRevisionConfigResponse setRevisionMergeEnabled(Boolean revisionMergeEnabled) {
        this.revisionMergeEnabled = revisionMergeEnabled;
        return this;
    }
    public Boolean getRevisionMergeEnabled() {
        return this.revisionMergeEnabled;
    }

    public BaseMultiRevisionConfigResponse setRevisionRecyclePeriod(Long revisionRecyclePeriod) {
        this.revisionRecyclePeriod = revisionRecyclePeriod;
        return this;
    }
    public Long getRevisionRecyclePeriod() {
        return this.revisionRecyclePeriod;
    }

}
