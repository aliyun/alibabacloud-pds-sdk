// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * share detail response
 */
public class ShareDetailResponse extends TeaModel {
    /**
     * <p>企业未配置独立域名时，允许的访问次数</p>
     */
    @NameInMap("access_quota")
    public Long accessQuota;

    /**
     * <p>企业未配置独立域名时，是否超过允许的访问次数</p>
     */
    @NameInMap("exceed_access_quota")
    public Boolean exceedAccessQuota;

    public static ShareDetailResponse build(java.util.Map<String, ?> map) throws Exception {
        ShareDetailResponse self = new ShareDetailResponse();
        return TeaModel.build(map, self);
    }

    public ShareDetailResponse setAccessQuota(Long accessQuota) {
        this.accessQuota = accessQuota;
        return this;
    }
    public Long getAccessQuota() {
        return this.accessQuota;
    }

    public ShareDetailResponse setExceedAccessQuota(Boolean exceedAccessQuota) {
        this.exceedAccessQuota = exceedAccessQuota;
        return this;
    }
    public Boolean getExceedAccessQuota() {
        return this.exceedAccessQuota;
    }

}
