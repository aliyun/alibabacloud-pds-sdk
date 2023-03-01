// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class DomainEndpointsResponse extends TeaModel {
    @NameInMap("api_endpoint")
    public String apiEndpoint;

    @NameInMap("api_vpc_endpoint")
    public String apiVpcEndpoint;

    @NameInMap("app_endpoint")
    public String appEndpoint;

    @NameInMap("auth_endpoint")
    public String authEndpoint;

    @NameInMap("mgmt_endpoint")
    public String mgmtEndpoint;

    @NameInMap("store_list")
    public java.util.List<BaseStoreInfoResponse> storeList;

    @NameInMap("va_store_list")
    public java.util.List<BaseStoreInfoResponse> vaStoreList;

    @NameInMap("web_office_endpoint_list")
    public java.util.List<String> webOfficeEndpointList;

    public static DomainEndpointsResponse build(java.util.Map<String, ?> map) throws Exception {
        DomainEndpointsResponse self = new DomainEndpointsResponse();
        return TeaModel.build(map, self);
    }

    public DomainEndpointsResponse setApiEndpoint(String apiEndpoint) {
        this.apiEndpoint = apiEndpoint;
        return this;
    }
    public String getApiEndpoint() {
        return this.apiEndpoint;
    }

    public DomainEndpointsResponse setApiVpcEndpoint(String apiVpcEndpoint) {
        this.apiVpcEndpoint = apiVpcEndpoint;
        return this;
    }
    public String getApiVpcEndpoint() {
        return this.apiVpcEndpoint;
    }

    public DomainEndpointsResponse setAppEndpoint(String appEndpoint) {
        this.appEndpoint = appEndpoint;
        return this;
    }
    public String getAppEndpoint() {
        return this.appEndpoint;
    }

    public DomainEndpointsResponse setAuthEndpoint(String authEndpoint) {
        this.authEndpoint = authEndpoint;
        return this;
    }
    public String getAuthEndpoint() {
        return this.authEndpoint;
    }

    public DomainEndpointsResponse setMgmtEndpoint(String mgmtEndpoint) {
        this.mgmtEndpoint = mgmtEndpoint;
        return this;
    }
    public String getMgmtEndpoint() {
        return this.mgmtEndpoint;
    }

    public DomainEndpointsResponse setStoreList(java.util.List<BaseStoreInfoResponse> storeList) {
        this.storeList = storeList;
        return this;
    }
    public java.util.List<BaseStoreInfoResponse> getStoreList() {
        return this.storeList;
    }

    public DomainEndpointsResponse setVaStoreList(java.util.List<BaseStoreInfoResponse> vaStoreList) {
        this.vaStoreList = vaStoreList;
        return this;
    }
    public java.util.List<BaseStoreInfoResponse> getVaStoreList() {
        return this.vaStoreList;
    }

    public DomainEndpointsResponse setWebOfficeEndpointList(java.util.List<String> webOfficeEndpointList) {
        this.webOfficeEndpointList = webOfficeEndpointList;
        return this;
    }
    public java.util.List<String> getWebOfficeEndpointList() {
        return this.webOfficeEndpointList;
    }

}
