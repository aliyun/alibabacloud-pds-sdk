// This file is auto-generated, don't edit it. Thanks.

using System;
using System.Collections.Generic;
using System.IO;

using Tea;

namespace Aliyun.SDK.PDS.Client.Models
{
    /**
     * 
     */
    public class ImageMediaResponse : TeaModel {
        /// <summary>
        /// address_line
        /// </summary>
        [NameInMap("address_line")]
        [Validation(Required=false)]
        public string AddressLine { get; set; }

        /// <summary>
        /// city
        /// </summary>
        [NameInMap("city")]
        [Validation(Required=false)]
        public string City { get; set; }

        /// <summary>
        /// country
        /// </summary>
        [NameInMap("country")]
        [Validation(Required=false)]
        public string Country { get; set; }

        /// <summary>
        /// cropping_suggestion
        /// </summary>
        [NameInMap("cropping_suggestion")]
        [Validation(Required=false)]
        public List<CroppingSuggestionItem> CroppingSuggestion { get; set; }

        /// <summary>
        /// district
        /// </summary>
        [NameInMap("district")]
        [Validation(Required=false)]
        public string District { get; set; }

        /// <summary>
        /// exif json string
        /// </summary>
        [NameInMap("exif")]
        [Validation(Required=false)]
        public string Exif { get; set; }

        /// <summary>
        /// faces json string
        /// </summary>
        [NameInMap("faces")]
        [Validation(Required=false)]
        public string Faces { get; set; }

        /// <summary>
        /// height
        /// </summary>
        [NameInMap("height")]
        [Validation(Required=false)]
        public long? Height { get; set; }

        [NameInMap("image_quality")]
        [Validation(Required=false)]
        public ImageQuality ImageQuality { get; set; }

        /// <summary>
        /// system_tags
        /// </summary>
        [NameInMap("image_tags")]
        [Validation(Required=false)]
        public List<SystemTag> ImageTags { get; set; }

        /// <summary>
        /// location
        /// </summary>
        [NameInMap("location")]
        [Validation(Required=false)]
        public string Location { get; set; }

        /// <summary>
        /// province
        /// </summary>
        [NameInMap("province")]
        [Validation(Required=false)]
        public string Province { get; set; }

        /// <summary>
        /// story_image_score
        /// </summary>
        [NameInMap("story_image_score")]
        [Validation(Required=false)]
        public double? StoryImageScore { get; set; }

        /// <summary>
        /// time
        /// </summary>
        [NameInMap("time")]
        [Validation(Required=false)]
        public string Time { get; set; }

        /// <summary>
        /// township
        /// </summary>
        [NameInMap("township")]
        [Validation(Required=false)]
        public string Township { get; set; }

        /// <summary>
        /// width
        /// </summary>
        [NameInMap("width")]
        [Validation(Required=false)]
        public long? Width { get; set; }

    }

}
