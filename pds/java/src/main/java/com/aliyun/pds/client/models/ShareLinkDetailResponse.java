// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * share_link detail response
 */
public class ShareLinkDetailResponse extends TeaModel {
    // 企业未配置独立域名时，允许的访问次数
    @NameInMap("access_quota")
    public Long accessQuota;

    // 企业是否开通了分享可在线编辑的文档的功能
    @NameInMap("enable_office_editable")
    public Boolean enableOfficeEditable;

    // 企业未配置独立域名时，是否超过允许的访问次数
    @NameInMap("exceed_access_quota")
    public Boolean exceedAccessQuota;

    public static ShareLinkDetailResponse build(java.util.Map<String, ?> map) throws Exception {
        ShareLinkDetailResponse self = new ShareLinkDetailResponse();
        return TeaModel.build(map, self);
    }

    public ShareLinkDetailResponse setAccessQuota(Long accessQuota) {
        this.accessQuota = accessQuota;
        return this;
    }
    public Long getAccessQuota() {
        return this.accessQuota;
    }

    public ShareLinkDetailResponse setEnableOfficeEditable(Boolean enableOfficeEditable) {
        this.enableOfficeEditable = enableOfficeEditable;
        return this;
    }
    public Boolean getEnableOfficeEditable() {
        return this.enableOfficeEditable;
    }

    public ShareLinkDetailResponse setExceedAccessQuota(Boolean exceedAccessQuota) {
        this.exceedAccessQuota = exceedAccessQuota;
        return this;
    }
    public Boolean getExceedAccessQuota() {
        return this.exceedAccessQuota;
    }

}
