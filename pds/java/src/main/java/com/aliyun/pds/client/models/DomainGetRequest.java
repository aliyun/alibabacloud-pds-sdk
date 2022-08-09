// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * domain get request
 */
public class DomainGetRequest extends TeaModel {
    // 是否获取share/share_link详情
    @NameInMap("get_share_detail")
    public Boolean getShareDetail;

    // 是否 merge parent 配置
    @NameInMap("merge_parent")
    public Boolean mergeParent;

    public static DomainGetRequest build(java.util.Map<String, ?> map) throws Exception {
        DomainGetRequest self = new DomainGetRequest();
        return TeaModel.build(map, self);
    }

    public DomainGetRequest setGetShareDetail(Boolean getShareDetail) {
        this.getShareDetail = getShareDetail;
        return this;
    }
    public Boolean getGetShareDetail() {
        return this.getShareDetail;
    }

    public DomainGetRequest setMergeParent(Boolean mergeParent) {
        this.mergeParent = mergeParent;
        return this;
    }
    public Boolean getMergeParent() {
        return this.mergeParent;
    }

}
