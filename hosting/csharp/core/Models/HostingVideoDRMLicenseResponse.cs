// This file is auto-generated, don't edit it. Thanks.

using System;
using System.Collections.Generic;
using System.IO;

using Tea;

namespace Aliyun.SDK.Hosting.Client.Models
{
    /**
     * DRM License response
     */
    public class HostingVideoDRMLicenseResponse : TeaModel {
        /// <summary>
        /// drm_data
        /// </summary>
        [NameInMap("data")]
        [Validation(Required=true)]
        public string Data { get; set; }

        /// <summary>
        /// device_info
        /// </summary>
        [NameInMap("device_info")]
        [Validation(Required=true)]
        public string DeviceInfo { get; set; }

        /// <summary>
        /// states
        /// </summary>
        [NameInMap("states")]
        [Validation(Required=true)]
        public long? States { get; set; }

    }

}
