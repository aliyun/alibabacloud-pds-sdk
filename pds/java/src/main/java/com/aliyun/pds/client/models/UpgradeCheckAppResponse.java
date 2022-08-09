// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 *
 */
public class UpgradeCheckAppResponse extends TeaModel {
    // option
    @NameInMap("option")
    public String option;

    // release_date
    @NameInMap("release_date")
    public String releaseDate;

    // release_notes_url
    @NameInMap("release_notes_url")
    public String releaseNotesUrl;

    // url
    @NameInMap("url")
    public String url;

    // version
    @NameInMap("version")
    public String version;

    public static UpgradeCheckAppResponse build(java.util.Map<String, ?> map) throws Exception {
        UpgradeCheckAppResponse self = new UpgradeCheckAppResponse();
        return TeaModel.build(map, self);
    }

    public UpgradeCheckAppResponse setOption(String option) {
        this.option = option;
        return this;
    }
    public String getOption() {
        return this.option;
    }

    public UpgradeCheckAppResponse setReleaseDate(String releaseDate) {
        this.releaseDate = releaseDate;
        return this;
    }
    public String getReleaseDate() {
        return this.releaseDate;
    }

    public UpgradeCheckAppResponse setReleaseNotesUrl(String releaseNotesUrl) {
        this.releaseNotesUrl = releaseNotesUrl;
        return this;
    }
    public String getReleaseNotesUrl() {
        return this.releaseNotesUrl;
    }

    public UpgradeCheckAppResponse setUrl(String url) {
        this.url = url;
        return this;
    }
    public String getUrl() {
        return this.url;
    }

    public UpgradeCheckAppResponse setVersion(String version) {
        this.version = version;
        return this;
    }
    public String getVersion() {
        return this.version;
    }

}
