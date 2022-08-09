// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * domain get request
 */
public class DomainGetRequest extends TeaModel {
    // fields,需要获取的属性字段,英文逗号分隔,*表示获取所有fields支持的枚举属性字段,为空不获取任何枚举属性字段
    @NameInMap("fields")
    public String fields;

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

    public DomainGetRequest setFields(String fields) {
        this.fields = fields;
        return this;
    }
    public String getFields() {
        return this.fields;
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
