// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * get_share_token request
 */
public class GetShareLinkTokenRequest extends TeaModel {
    @NameInMap("httpheaders")
    public java.util.Map<String, String> httpheaders;

    // addition_data
    @NameInMap("addition_data")
    public java.util.Map<String, ?> additionData;

    // check_share_pwd, effective for creator, admin or aksk only
    @NameInMap("check_share_pwd")
    public Boolean checkSharePwd;

    // expire_sec
    @NameInMap("expire_sec")
    @Validation(maximum = 7200)
    public Long expireSec;

    @NameInMap("referer")
    public String referer;

    // share_id
    @NameInMap("share_id")
    public String shareId;

    // share_pwd
    @NameInMap("share_pwd")
    public String sharePwd;

    public static GetShareLinkTokenRequest build(java.util.Map<String, ?> map) throws Exception {
        GetShareLinkTokenRequest self = new GetShareLinkTokenRequest();
        return TeaModel.build(map, self);
    }

    public GetShareLinkTokenRequest setHttpheaders(java.util.Map<String, String> httpheaders) {
        this.httpheaders = httpheaders;
        return this;
    }
    public java.util.Map<String, String> getHttpheaders() {
        return this.httpheaders;
    }

    public GetShareLinkTokenRequest setAdditionData(java.util.Map<String, ?> additionData) {
        this.additionData = additionData;
        return this;
    }
    public java.util.Map<String, ?> getAdditionData() {
        return this.additionData;
    }

    public GetShareLinkTokenRequest setCheckSharePwd(Boolean checkSharePwd) {
        this.checkSharePwd = checkSharePwd;
        return this;
    }
    public Boolean getCheckSharePwd() {
        return this.checkSharePwd;
    }

    public GetShareLinkTokenRequest setExpireSec(Long expireSec) {
        this.expireSec = expireSec;
        return this;
    }
    public Long getExpireSec() {
        return this.expireSec;
    }

    public GetShareLinkTokenRequest setReferer(String referer) {
        this.referer = referer;
        return this;
    }
    public String getReferer() {
        return this.referer;
    }

    public GetShareLinkTokenRequest setShareId(String shareId) {
        this.shareId = shareId;
        return this;
    }
    public String getShareId() {
        return this.shareId;
    }

    public GetShareLinkTokenRequest setSharePwd(String sharePwd) {
        this.sharePwd = sharePwd;
        return this;
    }
    public String getSharePwd() {
        return this.sharePwd;
    }

}
