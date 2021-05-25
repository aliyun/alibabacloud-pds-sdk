// This file is auto-generated, don't edit it. Thanks.

using System;
using System.Collections.Generic;
using System.IO;

using Tea;

namespace Aliyun.SDK.PDS.Client.Models
{
    /**
     * Search image address groups request
     */
    public class SearchImageAddressGroupsRequest : TeaModel {
        [NameInMap("headers")]
        [Validation(Required=false)]
        public Dictionary<string, string> Headers { get; set; }

        /// <summary>
        /// 查询的地点级别
        /// </summary>
        [NameInMap("address_level")]
        [Validation(Required=false)]
        public string AddressLevel { get; set; }

        /// <summary>
        /// 查询的地点数组
        /// </summary>
        [NameInMap("address_names")]
        [Validation(Required=false)]
        public List<string> AddressNames { get; set; }

        /// <summary>
        /// br_geo_point
        /// </summary>
        [NameInMap("br_geo_point")]
        [Validation(Required=false)]
        public string BrGeoPoint { get; set; }

        /// <summary>
        /// Drive ID
        /// </summary>
        [NameInMap("drive_id")]
        [Validation(Required=true)]
        public string DriveId { get; set; }

        /// <summary>
        /// image_thumbnail_process
        /// </summary>
        [NameInMap("image_thumbnail_process")]
        [Validation(Required=false)]
        public string ImageThumbnailProcess { get; set; }

        /// <summary>
        /// tl_geo_point
        /// </summary>
        [NameInMap("tl_geo_point")]
        [Validation(Required=false)]
        public string TlGeoPoint { get; set; }

        /// <summary>
        /// video_thumbnail_process
        /// </summary>
        [NameInMap("video_thumbnail_process")]
        [Validation(Required=false)]
        public string VideoThumbnailProcess { get; set; }

    }

}
