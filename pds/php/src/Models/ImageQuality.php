<?php

// This file is auto-generated, don't edit it. Thanks.

namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

class ImageQuality extends Model
{
    /**
     * @var int
     */
    public $clarity;

    /**
     * @var int
     */
    public $clarityScore;

    /**
     * @var int
     */
    public $color;

    /**
     * @var int
     */
    public $colorScore;

    /**
     * @var int
     */
    public $compositionScore;

    /**
     * @var int
     */
    public $contrast;

    /**
     * @var int
     */
    public $contrastScore;

    /**
     * @var int
     */
    public $exposure;

    /**
     * @var int
     */
    public $exposureScore;

    /**
     * @var int
     */
    public $overallScore;
    protected $_name = [
        'clarity'          => 'clarity',
        'clarityScore'     => 'clarity_score',
        'color'            => 'color',
        'colorScore'       => 'color_score',
        'compositionScore' => 'composition_score',
        'contrast'         => 'contrast',
        'contrastScore'    => 'contrast_score',
        'exposure'         => 'exposure',
        'exposureScore'    => 'exposure_score',
        'overallScore'     => 'overall_score',
    ];

    public function validate()
    {
    }

    public function toMap()
    {
        $res = [];
        if (null !== $this->clarity) {
            $res['clarity'] = $this->clarity;
        }
        if (null !== $this->clarityScore) {
            $res['clarity_score'] = $this->clarityScore;
        }
        if (null !== $this->color) {
            $res['color'] = $this->color;
        }
        if (null !== $this->colorScore) {
            $res['color_score'] = $this->colorScore;
        }
        if (null !== $this->compositionScore) {
            $res['composition_score'] = $this->compositionScore;
        }
        if (null !== $this->contrast) {
            $res['contrast'] = $this->contrast;
        }
        if (null !== $this->contrastScore) {
            $res['contrast_score'] = $this->contrastScore;
        }
        if (null !== $this->exposure) {
            $res['exposure'] = $this->exposure;
        }
        if (null !== $this->exposureScore) {
            $res['exposure_score'] = $this->exposureScore;
        }
        if (null !== $this->overallScore) {
            $res['overall_score'] = $this->overallScore;
        }

        return $res;
    }

    /**
     * @param array $map
     *
     * @return ImageQuality
     */
    public static function fromMap($map = [])
    {
        $model = new self();
        if (isset($map['clarity'])) {
            $model->clarity = $map['clarity'];
        }
        if (isset($map['clarity_score'])) {
            $model->clarityScore = $map['clarity_score'];
        }
        if (isset($map['color'])) {
            $model->color = $map['color'];
        }
        if (isset($map['color_score'])) {
            $model->colorScore = $map['color_score'];
        }
        if (isset($map['composition_score'])) {
            $model->compositionScore = $map['composition_score'];
        }
        if (isset($map['contrast'])) {
            $model->contrast = $map['contrast'];
        }
        if (isset($map['contrast_score'])) {
            $model->contrastScore = $map['contrast_score'];
        }
        if (isset($map['exposure'])) {
            $model->exposure = $map['exposure'];
        }
        if (isset($map['exposure_score'])) {
            $model->exposureScore = $map['exposure_score'];
        }
        if (isset($map['overall_score'])) {
            $model->overallScore = $map['overall_score'];
        }

        return $model;
    }
}
