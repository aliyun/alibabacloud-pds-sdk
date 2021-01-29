// This file is auto-generated, don't edit it. Thanks.

using System;
using System.Collections.Generic;
using System.IO;

using Tea;

namespace Aliyun.SDK.PDS.Client.Models
{
    /**
     * 获取office文档在线编辑地址 response
     */
    public class GetOfficeEditUrlResponse : TeaModel {
        /// <summary>
        /// EditUrl
        /// </summary>
        [NameInMap("edit_url")]
        [Validation(Required=false)]
        public string EditUrl { get; set; }

        /// <summary>
        /// AccessToken
        /// </summary>
        [NameInMap("office_access_token")]
        [Validation(Required=false)]
        public string OfficeAccessToken { get; set; }

        /// <summary>
        /// RefreshToken
        /// </summary>
        [NameInMap("office_refresh_token")]
        [Validation(Required=false)]
        public string OfficeRefreshToken { get; set; }

    }

}
