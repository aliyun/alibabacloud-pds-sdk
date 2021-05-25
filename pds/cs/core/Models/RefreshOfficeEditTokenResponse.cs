// This file is auto-generated, don't edit it. Thanks.

using System;
using System.Collections.Generic;
using System.IO;

using Tea;

namespace Aliyun.SDK.PDS.Client.Models
{
    /**
     * 刷新office文档在线编辑凭证 response
     */
    public class RefreshOfficeEditTokenResponse : TeaModel {
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
