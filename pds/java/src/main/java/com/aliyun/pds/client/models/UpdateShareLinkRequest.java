// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * update_share_link request
 */
public class UpdateShareLinkRequest extends TeaModel {
    @NameInMap("httpheaders")
    public java.util.Map<String, String> httpheaders;

    // description
    @NameInMap("description")
    public String description;

    // expiration
    @NameInMap("expiration")
    public String expiration;

    // is_subscribed
    @NameInMap("is_subscribed")
    public Boolean isSubscribed;

    // num_of_subscribers
    @NameInMap("num_of_subscribers")
    public Long numOfSubscribers;

    // share_id
    @NameInMap("share_id")
    public String shareId;

    // share_name
    @NameInMap("share_name")
    public String shareName;

    // share_pwd
    @NameInMap("share_pwd")
    public String sharePwd;

    // status
    @NameInMap("status")
    public String status;

    public static UpdateShareLinkRequest build(java.util.Map<String, ?> map) throws Exception {
        UpdateShareLinkRequest self = new UpdateShareLinkRequest();
        return TeaModel.build(map, self);
    }

    public UpdateShareLinkRequest setHttpheaders(java.util.Map<String, String> httpheaders) {
        this.httpheaders = httpheaders;
        return this;
    }
    public java.util.Map<String, String> getHttpheaders() {
        return this.httpheaders;
    }

    public UpdateShareLinkRequest setDescription(String description) {
        this.description = description;
        return this;
    }
    public String getDescription() {
        return this.description;
    }

    public UpdateShareLinkRequest setExpiration(String expiration) {
        this.expiration = expiration;
        return this;
    }
    public String getExpiration() {
        return this.expiration;
    }

    public UpdateShareLinkRequest setIsSubscribed(Boolean isSubscribed) {
        this.isSubscribed = isSubscribed;
        return this;
    }
    public Boolean getIsSubscribed() {
        return this.isSubscribed;
    }

    public UpdateShareLinkRequest setNumOfSubscribers(Long numOfSubscribers) {
        this.numOfSubscribers = numOfSubscribers;
        return this;
    }
    public Long getNumOfSubscribers() {
        return this.numOfSubscribers;
    }

    public UpdateShareLinkRequest setShareId(String shareId) {
        this.shareId = shareId;
        return this;
    }
    public String getShareId() {
        return this.shareId;
    }

    public UpdateShareLinkRequest setShareName(String shareName) {
        this.shareName = shareName;
        return this;
    }
    public String getShareName() {
        return this.shareName;
    }

    public UpdateShareLinkRequest setSharePwd(String sharePwd) {
        this.sharePwd = sharePwd;
        return this;
    }
    public String getSharePwd() {
        return this.sharePwd;
    }

    public UpdateShareLinkRequest setStatus(String status) {
        this.status = status;
        return this;
    }
    public String getStatus() {
        return this.status;
    }

}
